from rest_framework import serializers
from .models import InteractiveMap

class InteractiveMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractiveMap
        fields = ('id', 'coordinates', 'type_of_poison', 'cleared')