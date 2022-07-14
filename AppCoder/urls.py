from django.urls import path
from AppCoder.views import mostrar_nombre,inicio

urlpatterns = [
    
    path('listar_nombres/', mostrar_nombre ),
    path('inicio/', inicio),
]