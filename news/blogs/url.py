from django.urls import path
from . import views

urlpatterns = [


    path('', views.index,name='index'),
    path('about', views.about),
    path('crud', views.crud,name='crud'),
    path('news/<id>', views.news_details,name='news'),
    path('add-comments', views.news_comments,name='add-comments'),
    path('delete/<crud_id>', views.delete_record),
    path('edit/<crud_id>', views.edit_record),
    path('contact', views.contact,name='contact'),
    path('gallery', views.gallery,name='gallery')

    
    
       
]
