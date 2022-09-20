from django.urls import path
from .import views
 
app_name = 'blogs'

urlpatterns = [
    
    path('getlist/',views.blog_list , name='createBlog'),
    path('create/',views.create_blog , name='createBlog'),
    path('getdetail/<int:pk>', views.getBlogDetail, name='blogDetail'),
    path('update/<int:pk>', views.update_blog, name='updateBlog'),
    path('delete/<int:pk>', views.delete_blog, name='deleteBlog'),
     
]