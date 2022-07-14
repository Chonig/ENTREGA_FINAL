from django.urls import path
from AppCoder.views import *

urlpatterns = [
    
    path('listar_nombres/', mostrar_nombre ),
    path('inicio/', inicio),
]