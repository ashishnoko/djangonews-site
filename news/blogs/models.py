from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=200,unique=True)


    def __str__(self):
        return self.cat_name

class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news')
    description = models.TextField()
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    page_visit = models.IntegerField(default=0)
     
    class Meta:
         verbose_name = 'New' 



    def __str__(self):
        return self.title 
    

class Comments(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    website =  models.CharField(max_length=200)
    comments = models.TextField()
    news_id = models.ForeignKey(News,on_delete=CASCADE)
        
        
    def __str__(self):
        return self.name


class Crud(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    number =  models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject =  models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    photo =  models.ImageField(upload_to='gallery')

    
