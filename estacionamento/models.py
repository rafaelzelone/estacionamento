from django.db import models
from django.urls import reverse

class Carro(models.Model):
    placa = models.CharField(max_length=7)
    slug = models.SlugField(max_length=7, unique=True)
    modelo = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    proprietario = models.CharField(max_length=40)
    hora =  models.FloatField(max_length=2)
    minutos = models.FloatField(max_length=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.placa

    def get_absolute_url(self):
        return reverse("estacionamento:detail", kwargs={"slug": self.slug})
    
    def getpreco(self):
        return(20)
    

   
