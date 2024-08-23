from django.db import models

class Email(models.Model):
    content = models.TextField()

    def __str__(self):
        # Return the first 50 characters of the email content
        return self.content[:50] or "No content"

class EmailAnalysis(models.Model):
    # email = models.ForeignKey(Email, on_delete=models.CASCADE)
    content = models.TextField()
    sentiment_huggingface = models.CharField(max_length=255, blank=True, null=True)
    
    sentiment_berttweet = models.CharField(max_length=255, blank=True,null=True)

    # def __str__(self):
    #     # Return a string representation of the Email ID and sentiment
    #     return f"Email ID: {self.email.id} - Sentiment: {self.sentiment or 'No sentiment'}"

class Test(models.Model):
    content = models.TextField()
