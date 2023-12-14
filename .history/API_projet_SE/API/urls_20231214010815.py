from django.urls import path
from .views import MusiqueListCreateAPIView, MusiqueDetailAPIView
from . import views

app_name = "API"

urlpatterns = [
    path('musiques/', MusiqueListCreateAPIView.as_view(), name='musique-list'),
    path('musiques/<int:pk>/', MusiqueDetailAPIView.as_view(), name='musique-detail'),
    path('musique/<int:id>/fichier-audio/', views.getSongData.as_view(), name='musique-fichier-audio1'),
    # Ajoutez d'autres URLs selon vos besoins
]
