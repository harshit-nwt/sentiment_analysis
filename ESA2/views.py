
from django.shortcuts import render
# from ESA.langchain_service import get_berttweet_result
from ESA2.tasks import sentiment_analyzed

def esa2(request):
    if request.method=='POST':
        email_content1 = request.POST.get('email_content1')
        email_content2 = request.POST.get('email_content2')
        email_content3 = request.POST.get('email_content3')
        email_content4 = request.POST.get('email_content4')
        email_content5 = request.POST.get('email_content5')

        result1=sentiment_analyzed.delay( email_content1)
        result2=sentiment_analyzed.delay( email_content2)
        result3=sentiment_analyzed.delay( email_content3)
        result4=sentiment_analyzed.delay( email_content4)
        result5=sentiment_analyzed.delay( email_content5)

        

        print('results:',result1.get(),result2.get(),result3.get(),result4.get(),result5.get())
        context={'result1':result1.get(),'result2':result2.get(),'result3':result3.get(),'result4':result4.get(),'result5':result5.get()}

        return render(request,'esa2.html',context)
    return render(request, 'esa2.html')
# Create your views here.


# Create your views here.
