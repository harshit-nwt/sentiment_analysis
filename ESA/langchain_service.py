# your_app/langchain_service.py
import openai
from django.conf import settings

# Set up your OpenAI API key
openai.api_key = settings.OPENAI_API_KEY

def analyze_sentiment(text):
    # Create a prompt for categorization
    prompt = (
        "Categorize the following email into one of the following categories: "
        "'Complaint', 'Feedback', 'Request'. If none of these fit, return 'Other'.'along with probability.'also print the time consumed.'\n\n"
        f"Email: {text}\n\n"
        "Category:"
    )
    
    # Generate a response using the OpenAI model
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # or another supported model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extract and return the category from the response
    return response['choices'][0]['message']['content'].strip()
