
from django.urls import path
from .import views
 
app_name = 'reviews'

urlpatterns = [
    
    path('list/',views.review_list , name='createBlog'),
    path('create/',views.create_review , name='createBlog'),
    
     
]