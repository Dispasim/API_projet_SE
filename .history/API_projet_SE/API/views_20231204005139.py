from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Musique
from .serializers import MusiqueSerializer

class MusiqueListCreateAPIView(generics.ListCreateAPIView):
    queryset = Musique.objects.all()
    serializer_class = MusiqueSerializer

class MusiqueDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musique.objects.all()
    serializer_class = MusiqueSerializer

