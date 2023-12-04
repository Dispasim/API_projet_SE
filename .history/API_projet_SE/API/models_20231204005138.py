from django.db import models

# Create your models here.


class Musique(models.Model):
    titre = models.CharField(max_length=100)
    artiste = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    duree = models.DurationField()
    fichier_audio = models.FileField(upload_to='musiques/')