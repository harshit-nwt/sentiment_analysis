from django.shortcuts import render
from django.http import HttpResponse
# import openai
from django.conf import settings
from .models import EmailAnalysis,Email
from .langchain_service import get_huggingface_result,get_berttweet_result

# openai.api_key = settings.OPENAI_API_KEY
def email_sentiment_analysis(request):
    if request.method == 'POST':
        email_content = request.POST.get('email_content')
        # sentiment = analyze_sentiment(email_content)
        sentiment_hf= get_huggingface_result(email_content)
        sentiment_gbr = get_berttweet_result(email_content)
        sentiment_hf= get_huggingface_result(email_content)
        print(sentiment_hf)

        # print(f"Email Content: {email_content}")
        # print(f"Sentiment HF: {sentiment_hf}")
        # print(f"Sentiment GBR: {sentiment_gbr}")
        # return render(request, 'results.html', {'sentiment': sentiment})
        # return render(request, 'email_analysis.html', {'emails': emails})

        # category = sentiment_hf.get('Category', 'Unknown')
        # print(category)
        # probability = float(sentiment_hf.get('Probability', 0.0))
        # print(probability)
        # time_consumed = float(sentiment_hf.get('Time_Consumed', 0.0))
        # print(time_consumed)


        # Save the analyzed result to the database
        EmailAnalysis.objects.create(
            content=email_content,
            sentiment_huggingface=sentiment_hf,
            sentiment_berttweet=sentiment_gbr,
            
            

        )
        
        



        return render(request, 'analyze_email.html', {'email_content':email_content,'sentiment_hf':sentiment_hf,'sentiment_gbr':sentiment_gbr})
    return render(request, 'analyze_email.html')

def email_list(request):
    # Fetch all emails along with their analysis
    # emails = Email.objects.all()[:50]
    # email_analysis = {email: EmailAnalysis.objects.filter(email=email).first() for email in emails}
    
    analyses = EmailAnalysis.objects.all()
      
  

    # Ensure that the return statement includes an HttpResponse object
    return render(request, 'email_list.html', {'analyses': analyses})


