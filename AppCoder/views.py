from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.views import *
from AppCoder.models import Persona




def inicio(request):

    return render( request, "AppCoder/index.html",{})
    


def mostrar_nombre (request):
    
    context = {"nombre": Persona.objects.all(), "apellido": Persona.objects.all()}

    return render ( request, "AppCoder/mostrar_personas.html", context)



def mostrar_contacto (request):
    pass



def mostrar_info(request):
    pass



