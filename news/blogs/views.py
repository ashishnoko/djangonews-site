from django.shortcuts import render,HttpResponse,redirect
from .models import Contact, Crud, Gallery, News,Comments,Crud
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator






def index(request): 
    News_list = News.objects.all()
    paginator = Paginator(News_list, 3) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
        
    content={
        'newsData': page_obj,
        'page_obj':   page_obj
    }
    return render(request,'index.html',content)

def about(request):
    return render(request,'about.html')



def news_details(request,id):
    np = News.objects.get(id=id)
    np.page_visit+=1
    np.save()
    content ={
        'newsData':News.objects.get(id=id),
        'commentData':Comments.objects.filter(news_id=id )
    }
    return render(request,'news.html',content)

def news_comments(request):
    if request.method == 'POST':
       
       
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
        comments = request.POST['message']
        news_id = request.POST['news_id']
        Comments.objects.create(name=name,email=email,website=website,comments=comments,news_id=News.objects.get(id=news_id),)

   
        return redirect( request.META.get('HTTP_REFERER','/'))



def crud(request):
    if request.method == "POST":
        obj = Crud()
        obj.name= request.POST['name']
        obj.address= request.POST['address']
        obj.number= request.POST['number']
        obj.message= request.POST['message']
        obj.save()
        messages.success(request,'Data was inserted')

        return redirect('crud')
    
    else:
        content={
            'crudData':Crud.objects.all()

        }
        return render(request,'crud.html',content)

    
 
def delete_record(request,crud_id):
    find_record = Crud.objects.get(id=crud_id).delete()
    messages.success(request,'Student was deleted')
    return redirect('crud')


def edit_record(request,crud_id):
    a_object =   Crud.objects.get(id=crud_id)

    if request.method == "POST":
        a_object.name= request.POST['name']
        a_object.address= request.POST['address']
        a_object.number= request.POST['number']
        a_object.message= request.POST['message']
        a_object.save()
        messages.success(request,'Data was updated')

        return redirect('crud')

        
        
    content = {
        'crudData':a_object

    }
    return render(request,'edit.html',content)


def contact(request):
    
    if request.method == "POST":
        name= request.POST['name']
        email = request.POST['email']
        subject= request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(name=name,email=email,subject=subject,message=message)
        send_mail(subject, message, email, ['laravel3pm@gmail.com'])
        send_mail('thank for the contact', 'welcome to the django','laravel3pm@gmail.com',[email])
        messages.success(request,'Mail was sent')
        return redirect('contact')

    else:

        return render(request,'contact.html')



def gallery(request):
   
    
     return render(request,'gallery.html')



    


