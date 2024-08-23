from django.core.management.base import BaseCommand
from ESA.models import Email, EmailAnalysis
from ESA.langchain_service import analyze_sentiment

class Command(BaseCommand):
    help = 'Categorize emails using OpenAI and update the database'

    def handle(self, *args, **kwargs):
        # Fetch the first 50 emails that do not have associated analysis
        emails = Email.objects.all()[:50]  # Limit to 50 emails
        
        for email in emails:
            # Check if there is already an analysis for this email
            analysis, created = EmailAnalysis.objects.get_or_create(
                email=email,
                defaults={'content': email.content}
            )
            
            if created:
                # Analyze sentiment if not already done
                sentiment_result = analyze_sentiment(email.content)
                
                # Extract sentiment and probability
                sentiment_category = sentiment_result.get("Category", "UNKNOWN")
                sentiment_probability = sentiment_result.get("Probability", 0.0)
                
                # Update analysis with sentiment and category
                analysis.sentiment = sentiment_category  # Assign the sentiment category to the field
                analysis.save()
                
                # Log the result
                self.stdout.write(self.style.SUCCESS(f'Processed email ID {email.id} with sentiment: {sentiment_category}'))
            else:
                # Log if the analysis already exists
                self.stdout.write(self.style.WARNING(f'Email ID {email.id} already analyzed.'))

