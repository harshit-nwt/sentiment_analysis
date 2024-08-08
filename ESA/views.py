#from django.shortcuts import render

# Create your views here.
# your_app/views.py
from django.shortcuts import render
from .langchain_service import analyze_sentiment

def email_sentiment_analysis(request):
    if request.method == 'POST':
        email_content = request.POST.get('email_content')
        sentiment = analyze_sentiment(email_content)
        return render(request, 'results.html', {'sentiment': sentiment})

    return render(request, 'analyze_email.html')



