from django.urls import path
from . import views

urlpatterns = [
    # Autres URL de votre application
    path('signup/', views.signup, name='signup'),
]
