from django.db import models
from django.contrib.auth.models import User




class Persona (models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} { self.apellido}"


class Articulo (models.Model):

    producto = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.producto}"


class Datos (models.Model):

    empresa = models.CharField(max_length=40)
    calle = models.CharField(max_length=40)
    altura = models.IntegerField()
    cant_empleados = models.IntegerField()

    def __str__(self):
        return f"{self.empresa}"


class Contacto (models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} { self.apellido}"



class Avatar(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    avatar = models.ImageField(upload_to= "avatars", null= True, blank= True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_upgrade = models.DateField(auto_now=True)

    def __str__ (self):
        return f"{self.user.username}"
