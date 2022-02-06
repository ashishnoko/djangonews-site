



from .models import Category

def global_data_send(self):

    content={
        'categoryData': Category.objects.all()
        
    }
    return content
