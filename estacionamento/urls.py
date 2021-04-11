from django.urls import path

from . import views

app_name = "estacionamento"


urlpatterns = [
    path("", views.CarroListView.as_view(), name="list"),
    path("entrada", views.EntradaCarroCreateView.as_view(), name="entrada"),
    
]