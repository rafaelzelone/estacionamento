from django.shortcuts import render
from django.views.generic import CreateView, ListView, DateDetailView
from .models import Carro


from .Form import EntradaCarros


class CarroListView(ListView):
    model = Carro

class CarroPostDetailView(DateDetailView):
    model = Carro


class EntradaCarroCreateView(CreateView):
    model = Carro
    form_class= EntradaCarros
    template_name = "estacionamento/Entrada.html"
    




     
