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

class MusiqueListCreateAPIView(generics.ListCreateAPIView):
    queryset = Musique.objects.all()
    serializer_class = MusiqueSerializer

class MusiqueDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musique.objects.all()
    serializer_class = MusiqueSerializer


        

        

class getSongData(APIView):
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



