from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)

class Lugar(models.Model):
    nombre = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    encargado = models.CharField(max_length=30) 

class Eventos(models.Model):
    nombre = models.CharField(max_length=30)
    lugar= models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    hora = models.CharField(max_length=30)
    responsable = models.CharField(max_length=30)     
    url = models.CharField(max_length=30)     
    

    