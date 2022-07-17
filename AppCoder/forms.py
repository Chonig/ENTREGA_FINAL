from django import forms


class FormularioReserva (forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()


class BusquedaPersona (forms.Form):

    criterio = forms.CharField()


class FormularioContacto (forms.Form):
    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    telefono = forms.IntegerField()





