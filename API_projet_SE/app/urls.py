from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    # Autres URL de votre application
    path('signup/', views.signup, name='signup'),
]
