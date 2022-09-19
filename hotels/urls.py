from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    path('viewHotel/', views.getHotel),
    path('viewHotel/<int:pk>', views.getHotel),
    path('createHotel/', views.createHotel),
    path('completeUpdate/<int:pk>', views.completeUpdateHotel),
    path('partialUpdate/<int:pk>', views.partialUpdateHotel),
    path('deleteHotel/<int:pk>', views.deleteHotel),

]
