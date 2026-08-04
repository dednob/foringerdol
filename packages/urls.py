from django.urls import path
from . import views

app_name = 'packages'

urlpatterns = [
    path('list/', views.get_packages),
    path('details/<str:slug>', views.get_packages),
    path('byevent/<int:eventid>', views.packages_by_event),
    path('create/', views.create_package),
    path('update/<int:pk>', views.complete_update_package),
    path('partialUpdate/<int:pk>', views.partial_update_package),
    path('delete/<int:pk>', views.delete_package),

]
