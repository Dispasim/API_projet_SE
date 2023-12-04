from django.shortcuts import render
import os
# Create your views here.
from rest_framework import generics
from .models import Musique
from .serializers import MusiqueSerializer
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404

class MusiqueListCreateAPIView(generics.ListCreateAPIView):
    queryset = Musique.objects.all()
    serializer_class = MusiqueSerializer

class MusiqueDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musique.objects.all()
    serializer_class = MusiqueSerializer

