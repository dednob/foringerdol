from django.urls import path
from .import views
 
app_name = 'pictures'

urlpatterns = [
    
    path('update/',views.update_picture , name='updatepictures'),
    path('getdetail/', views.get_pictures, name='PicturesDetail'),
    # path('create/',views.create_blog, name='createBlog'),
    # path('dashboard/count/',views.blog_list_count , name='getListcount'),
    
    # path('update/<int:pk>', views.update_blog, name='updateBlog'),
    # path('delete/<int:pk>', views.delete_blog, name='deleteBlog'),
     
]