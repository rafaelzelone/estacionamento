from django.contrib import admin

from .models import Carro

@admin.register(Carro)
class CarAdmin(admin.ModelAdmin):
    list_display = ("placa", "modelo", "proprietario", "data")
    prepopulated_fields= {"slug": ("placa",)}

