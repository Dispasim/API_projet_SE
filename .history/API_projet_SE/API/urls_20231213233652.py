from django.urls import path
from .views import MusiqueListCreateAPIView, MusiqueDetailAPIView, MusiqueFileView

app_name = "API"

urlpatterns = [
    path('musiques/', MusiqueListCreateAPIView.as_view(), name='musique-list'),
    path('musiques/<int:pk>/', MusiqueDetailAPIView.as_view(), name='musique-detail'),
    path('musique/<int:musique_id>/fichier-audio/', MusiqueFileView.as_view(), name='musique-fichier-audio'),
    # Ajoutez d'autres URLs selon vos besoins
]
