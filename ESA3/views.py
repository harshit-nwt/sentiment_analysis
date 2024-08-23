from django.shortcuts import render
# from  sentiment_nwt_project.celery import summ,sub
from ESA3.tasks import sub,add,multiply
import time
def esa3(request):
    if request.method == 'POST':
        
  
        num1=int(request.POST.get('number1'))
        num2=int(request.POST.get('number2'))
        mul=num1*num2
        # time.sleep(10)
        result1=add.delay(num1,num2)
        result2=sub.delay(num1,num2)
        result3=multiply.delay(num1,num2)
        print('Result1:',result1)
        print('Result2:',result2)
        print('Result3:',result3)
        return render(request, "esa3.html",{'mul':mul})
    return render(request , "esa3.html")
# Create your views here.
