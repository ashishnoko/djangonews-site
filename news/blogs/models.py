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


    def __str__(self):
        return self.title 