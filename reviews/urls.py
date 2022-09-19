
from django.urls import path
from .import views
 
app_name = 'reviews'

urlpatterns = [
    
    path('getreviewlist/',views.review_list , name='createBlog'),
    path('postreview/',views.create_review , name='createBlog'),
    
     
]