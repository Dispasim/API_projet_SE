from django.shortcuts import render
import os
# Create your views here.
from rest_framework import generics
from .models import Musique
from .serializers import MusiqueSerializer, ChansonSerializer
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from . import serializers
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class MusiqueListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Musique.objects.all()
    serializer_class = MusiqueSerializer

class MusiqueDetailAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Musique.objects.all()
    serializer_class = serializers.MusiqueInfoSerializer


        

        

class getSongData(APIView):
    permission_classes = [AllowAny]
    serializer_class = ChansonSerializer

    def get(self, request, id, *args, **kwargs):
        try:
            musique = Musique.objects.get(id=id) 
        except Musique.DoesNotExist:
            return Response({"message": "La musique n'existe pas"}, status=404)  
        if musique.fichier_audio:    
            path = musique.fichier_audio.path 
            try:

                return FileResponse(open(path, 'rb')) 
            except FileNotFoundError:
                return Response({"message": "Fichier audio introuvable"}, status=404)
        else:
            return Response({"message": "Aucun fichier audio associé à cette musique"}, status=404)



class CreationUtilisateur(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = serializers.UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            utilisateur = serializer.save()
            return Response("Utilisateur créé avec succès", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ConnexionUtilisateurView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Identifiants invalides'}, status=status.HTTP_401_UNAUTHORIZED)    
        

class GetMusiqueInfo(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.MusiqueInfoSerializer


class GetUserFromToken(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        token_key = request.query_params.get('token', None)
        
        if not token_key:
            return Response({'error': 'Token non fourni'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = Token.objects.get(key=token_key)
        except Token.DoesNotExist:
            return Response({'error': 'Token invalide'}, status=status.HTTP_404_NOT_FOUND)
        
        user = token.user
        user_data = {
            'id': user.id,
            
            
        }
        return Response(user_data, status=status.HTTP_200_OK)    


class APIListViewId(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = MusiqueSerializer

    def get_queryset(self):
        id = self.kwargs['auteur_id']  
        return Musique.objects.filter(auteur_id=id)


class MusiqueDeleteView(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Musique.objects.all()
    serializer_class = MusiqueSerializer
    lookup_field = 'id' 
