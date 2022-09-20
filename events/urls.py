from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('view/list/', views.get_events),
    path('view/<int:pk>', views.get_events),
    path('bylocation/<int:locationid>', views.events_by_location),
    path('create/', views.create_event),
    path('update/<int:pk>', views.complete_update_event),
    path('partialUpdate/<int:pk>', views.partial_update_event),
    path('delete/<int:pk>', views.delete_event),

]
