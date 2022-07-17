from django.db import models




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
        return f"{self.producto} { self.precio} {self.cantidad}"


class Datos (models.Model):

    empresa = models.CharField(max_length=40)
    calle = models.CharField(max_length=40)
    altura = models.IntegerField()
    cant_empleados = models.IntegerField()

    def __str__(self):
        return f"{self.empresa} { self.calle} {self.altura} {self.cant_empleados}"


class Contacto (models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} { self.apellido} {self.email} {self.telefono}"