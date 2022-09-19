from django.urls import path, include
from django.contrib import admin
from locations import views as location_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('locations/', include('locations.urls')),
    path('hotels/', include('hotels.urls')),
    path('events/', include('events.urls')),


    # path('detail/', product_views.product_detail, name="Product detail"),

]
