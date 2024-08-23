# your_app/langchain_service.py
from django.conf import settings
from transformers import pipeline
import time
import emoji

from .models import EmailAnalysis

def preprocess_text(text):
    return emoji.demojize(text)  # Convert emojis to text

def transform_berttweet_response(response):
    # Map BERTweet categories to Hugging Face format
    category_mapping = {
        'POS': 'POSITIVE',
        'NEG': 'NEGATIVE'
    }
    return {
        'Category': category_mapping.get(response['Category'], 'UNKNOWN'),
        'Probability': response['Probability'],
        'Time_Consumed': response['Time_Consumed']
    }

def get_huggingface_result(text):
    # Start timing
    text = preprocess_text(text)
    start_time = time.time()
    
    # Load the sentiment analysis pipeline
    sentiment_analysis = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
    
    # Analyze sentiment using the Hugging Face model
    result = sentiment_analysis(text)[0]
    
    # Stop timing
    end_time = time.time()
    time_consumed = end_time - start_time
    
    # Extract and return the result
    hf_result = {
        "Category": result['label'],
        "Probability": result['score'],
        "Time_Consumed": time_consumed
    }
    return hf_result

def get_berttweet_result(text):
    # Start timing
    text = preprocess_text(text)
    start_time = time.time()
    
    # Load the sentiment analysis pipeline for BERTweet model
    sentiment_analysis_berttweet = pipeline("text-classification", model="finiteautomata/bertweet-base-sentiment-analysis")
    
    # Analyze sentiment using the BERTweet model
    result_berttweet = sentiment_analysis_berttweet(text)[0]
    
    # Stop timing
    end_time = time.time()
    time_consumed = end_time - start_time
    
    # Extract and transform the result for BERTweet model
    raw_result = {
        "Category": result_berttweet['label'],
        "Probability": result_berttweet['score'],
        "Time_Consumed": time_consumed
    }
    bertweet_result = transform_berttweet_response(raw_result)
    return bertweet_result
