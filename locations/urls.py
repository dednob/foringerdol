from django.urls import path
from . import views

app_name = 'locations'

urlpatterns = [
    path('view/list/', views.view_location),
   
    path('view/by-category/<str:pk>', views.location_by_category),
    
    path('details/<str:slug>', views.view_location),
    path('create/', views.create_location),
    path('update/<int:pk>', views.complete_update),
    path('partialUpdate/<int:pk>', views.partial_update),
    path('delete/<int:pk>', views.delete_location),

]
