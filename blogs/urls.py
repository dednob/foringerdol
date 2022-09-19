from django.urls import path
from .import views
 
app_name = 'blogs'

urlpatterns = [
    
    path('getbloglist/',views.blog_list , name='createBlog'),
    path('createblog/',views.create_blog , name='createBlog'),
    path('getblogdetail/<int:pk>', views.getBlogDetail, name='blogDetail'),
    path('updateblog/<int:pk>', views.update_blog, name='updateBlog'),
    path('deleteblog/<int:pk>', views.delete_blog, name='deleteBlog'),
     
]