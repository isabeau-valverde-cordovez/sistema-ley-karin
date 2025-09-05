from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_denuncias, name='lista_denuncias'),
    path('nueva/', views.nueva_denuncia, name='nueva_denuncia'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
    path('contacto/', views.contacto, name='contacto'),
]