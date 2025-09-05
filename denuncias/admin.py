from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Denuncia

@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'tipo', 'estado', 'fecha_creacion']
    list_filter = ['tipo', 'estado', 'fecha_creacion']
    search_fields = ['descripcion', 'usuario__username']