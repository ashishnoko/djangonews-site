from django.shortcuts import render,HttpResponse
from .models import News 



# Create your views here.
def index(request):
    content={
        'newsData':News.objects.all()
    }
    return render(request,'index.html',content)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


