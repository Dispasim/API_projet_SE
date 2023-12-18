from django.urls import path
from .views import MusiqueListCreateAPIView, MusiqueDetailAPIView
from . import views
from .views import RegistrationView, LoginView, LogoutView,ChangePasswordView

app_name = "API"

urlpatterns = [
    path('musiques/', MusiqueListCreateAPIView.as_view(), name='musique-list'),
    path('musiques/<int:pk>/', MusiqueDetailAPIView.as_view(), name='musique-detail'),
    path('musique/<int:id>/fichier-audio/', views.getSongData.as_view(), name='musique-fichier-audio1'),
    path('creer_utilisateur/', views.CreationUtilisateur.as_view(), name='creer_utilisateur'),
    # Ajoutez d'autres URLs selon vos besoins
]
