from django.contrib import admin

# Register your models here.
 
from .models import *

admin.site.register(Category)

@admin.register(News)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','image','description']
    search_fields = ['title','description']
    list_per_page = 3


admin.site.register(Comments)

admin.site.register(Crud)

admin.site.register(Gallery)