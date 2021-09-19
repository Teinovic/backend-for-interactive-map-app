from django.shortcuts import render
from .serializers import InteractiveMapSerializer
from rest_framework import viewsets      
from .models import InteractiveMap                 

class InteractiveMapView(viewsets.ModelViewSet):  
    serializer_class = InteractiveMapSerializer
    queryset = InteractiveMap.objects.all()     