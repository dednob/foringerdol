from django.urls import path
from . import views

app_name = 'locations'

urlpatterns = [
    path('viewLocation/', views.location_api_viewLocation),
    path('viewLocation/<int:pk>', views.location_api_viewLocation),
    path('createLocation/', views.location_api_createLocation),
    path('completeUpdate/<int:pk>', views.location_api_completeUpdate),
    path('partialUpdate/<int:pk>', views.location_api_partialUpdate),
    path('deleteLocation/<int:pk>', views.location_api_delete),

]
