from rest_framework import serializers
from .models import Musique

class MusiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musique
        fields = '__all__'
