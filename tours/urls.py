from django.urls import path
from . import views

app_name = 'tours'

urlpatterns = [
    path('viewTour/', views.getTour),
    path('viewTour/<int:pk>', views.getTour),
    path('createTour/', views.createTour),
    path('completeUpdate/<int:pk>', views.completeUpdateTour),
    path('partialUpdate/<int:pk>', views.partialUpdateTour),
    path('deleteTour/<int:pk>', views.deleteTour),

]
