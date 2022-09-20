from django.urls import path
from . import views

app_name = 'tours'

urlpatterns = [
    path('view/list/', views.get_tour),
    path('details/<int:pk>', views.get_tour),
    path('bylocation/<int:locationid>', views.tours_by_location),
    path('create/', views.create_tour),
    path('update/<int:pk>', views.complete_update_tour),
    path('partialupdate/<int:pk>', views.partial_update_tour),
    path('delete/<int:pk>', views.delete_tour),

]
