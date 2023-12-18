from rest_framework import serializers
from .models import Musique
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
class MusiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musique
        fields = '__all__'

class ChansonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musique
        fields = ("fichier_audio")


class UtilisateurSerializer(serializers.Serializer):
    pseudo = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    mot_de_passe = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['pseudo'],
            email=validated_data['email'],
            password=validated_data['mot_de_passe']
        )

class MusiqueInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musique
        fields = ("id","titre","album","duree")