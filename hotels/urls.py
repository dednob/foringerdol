from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    path('list/', views.get_hotel),
    path('details/<int:pk>', views.get_hotel),
    path('bylocation/<int:locationid>', views.hotels_by_location),
    path('create/', views.create_hotel),
    path('update/<int:pk>', views.complete_update_hotel),
    path('partialUpdate/<int:pk>', views.partial_update_hotel),
    path('delete/<int:pk>', views.delete_hotel),

]
