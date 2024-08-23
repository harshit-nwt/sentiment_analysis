from celery import shared_task
# from time import sleep

@shared_task
def sub(x,y):
    return x-y
@shared_task
def add(x,y):
    return x+y
@shared_task
def multiply(x,y):
    return x*y
@shared_task
def clear_session_cache(id):
    print(f'Session Cache Cleared:{id}')
    return id