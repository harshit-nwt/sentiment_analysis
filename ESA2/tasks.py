from celery import shared_task
# from time import sleep
from ESA.langchain_service import get_berttweet_result

@shared_task(name='analysis_task')
def sentiment_analyzed(email_content):
    result=get_berttweet_result(email_content)
    return result
