from django.urls import path
from .views import MusiqueListCreateAPIView, MusiqueDetailAPIView
from . import views


app_name = "API"

urlpatterns = [
    path('musiques/', MusiqueListCreateAPIView.as_view(), name='musique-list'),
    path('musiques_detail/', MusiqueDetailAPIView.as_view(), name='musique-detail'),
    path('musique/<int:id>/fichier_audio/', views.getSongData.as_view(), name='musique-fichier-audio1'),
    path('creer_utilisateur/', views.CreationUtilisateur.as_view(), name='creer_utilisateur'),
    path('connexion/', views.ConnexionUtilisateurView.as_view(), name='connexion_utilisateur'),
    path('get_user_from_token/', views.GetUserFromToken.as_view(), name='get_user_from_token'),
    # Ajoutez d'autres URLs selon vos besoins
]
