from rest_framework import serializers
from .models import Musique
from django.contrib.auth import get_user_model
class MusiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musique
        fields = '__all__'

class ChansonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musique
        fields = ("fichier_audio")

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", )        