from django.urls import path
from .views import MusiqueListCreateAPIView, MusiqueDetailAPIView

app_name = "API"

urlpatterns = [
    path('musiques/', MusiqueListCreateAPIView.as_view(), name='musique-list'),
    path('musiques/<int:pk>/', MusiqueDetailAPIView.as_view(), name='musique-detail'),
    # Ajoutez d'autres URLs selon vos besoins
]
