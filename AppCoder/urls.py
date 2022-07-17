from django.contrib import admin
from django.urls import path
from AppCoder import views
from AppCoder.views import *

urlpatterns = [

    path('inicio/', views.Home, name= "inicio"),
    path('formulario/', views.formulario, name="formulario"),
    path('mostrar-personas/', views.mostrar_personas, name="mostrar-personas"),
    path('datos-empresa/', views.mostrar_datos, name="datos-empresa"),
    path('busquedapersona/', views.formulario_busqueda, name="busquedapersona"),
    path('mostrar-articulos/', views.mostrar_articulo, name="mostrar-articulos"),
    path('contacto/', views.contacto, name="contacto"),
        
]