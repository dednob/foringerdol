from django.urls import path
from .import views
 
app_name = 'booking'

urlpatterns = [
    
    path('getlist/',views.booking_list , name='getList'),
    path('create/',views.create_booking, name='createBooking'),
    path('getdetail/<int:pk>', views.get_booking_detail, name='bookingDetail'),
    path('delete/<int:pk>', views.delete_booking, name='deleteBooking'),
    path('status/toggle/', views.toggle_payment_status, name='togglestatus'),
     
]