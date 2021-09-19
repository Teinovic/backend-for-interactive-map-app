from django.contrib import admin
from django.urls import path,include               
from rest_framework import routers                 
from interactivemap import views                             

router = routers.DefaultRouter()                   
router.register(r'interactivemap', views.InteractiveMapView, 'interactivemap')  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))             
]