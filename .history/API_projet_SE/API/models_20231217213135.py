from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.


class Musique(models.Model):
    titre = models.CharField(max_length=100)
    artiste = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    duree = models.DurationField()
    fichier_audio = models.FileField(upload_to='musiques/')
    auteur = models.ForeignKey(User, on_delete = models.CASCADE,related_name = "musique",default=1)

