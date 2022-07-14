from django.forms import forms


class FormularioReserva (forms.form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    fecha = forms.DateField()
    cant_personas = forms.IntegerField()
    hora_reserva = forms.TimeField()