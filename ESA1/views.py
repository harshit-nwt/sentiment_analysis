from django.shortcuts import render
from ESA.langchain_service import get_huggingface_result

def esa1(request):
    if request.method=='POST':
        email_content = request.POST.get('email_content')
        print(email_content)
        hugging_face_model=get_huggingface_result(email_content)
        print(hugging_face_model)
        context={'email_content':email_content,'hugging_face_model':hugging_face_model}
        print(context)
        return render(request , "esa1.html",context)
    return render(request, "esa1.html")
# Create your views here.
