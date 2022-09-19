from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('viewEvent/', views.getEvent),
    path('viewEvent/<int:pk>', views.getEvent),
    path('createEvent/', views.createEvent),
    path('completeUpdate/<int:pk>', views.completeUpdateEvent),
    path('partialUpdate/<int:pk>', views.partialUpdateEvent),
    path('deleteEvent/<int:pk>', views.deleteEvent),

]
