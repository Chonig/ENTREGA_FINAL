from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Persona,Datos,Articulo, Contacto
from AppCoder.forms import FormularioReserva,BusquedaPersona, FormularioContacto




def Home(request):

    return render( request, "AppCoder/home.html",{})
    


def mostrar_personas (request):
    
    context = {"nombre": Persona.objects.all(), "apellido": Persona.objects.all()}

    return render ( request, "AppCoder/mostrar_personas.html", context)



def formulario (request):

    if request.method == "POST":

        formulario = FormularioReserva(request.POST)


        print(formulario)

        if formulario.is_valid:

            informacion = formulario.cleaned_data

            persona = Persona(nombre = informacion['nombre'], apellido = informacion ['apellido'], edad = informacion['edad'])

            persona.save()

            return render ( request, "AppCoder/home.html")

    else:
        
        formulario  = FormularioReserva()

    return render (request, "AppCoder/formulario.html", {"formulario": formulario})





def mostrar_articulo(request):

    context = {}

    context ['info'] = Articulo.objects.all()

    return render ( request, "AppCoder/mostrar_articulos.html", context)



def mostrar_datos ( request):

    context = {}

    context ['info'] = Datos.objects.all()

    return render ( request, "AppCoder/datos_empresa.html", context)




def formulario_busqueda(request):

    busqueda_formulario = BusquedaPersona()

    if request.GET:
    
        personas = Persona.objects.filter(nombre=busqueda_formulario["criterio"]).all()
        return render(request, "AppCoder/busqueda_persona.html", {"personas" : personas})


    return render(request ,"AppCoder/busqueda_persona.html",{"busqueda_formulario": busqueda_formulario})



def contacto (request):

    if request.method == "POST":

        contacto = FormularioContacto(request.POST)


        print(contacto)

        if contacto.is_valid:

            informacion = contacto.cleaned_data

            persona = Contacto( nombre = informacion ['nombre'], apellido = informacion ['apellido'], email = informacion['email'], telefono = informacion['telefono'])

            persona.save()

            return render ( request, "AppCoder/home.html")

    else:
        
        contacto  = FormularioContacto()

    return render (request, "AppCoder/contacto.html", {"contacto": contacto})
