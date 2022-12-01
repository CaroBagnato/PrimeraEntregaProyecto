from django.db import models

# Create your models here.

class Post(models.Model):
    nombre=models.CharField(max_length=40)
    autor=models.CharField(max_length=40)
    categoria=models.CharField(max_length=40)

class Categorias(models.Model):
    categoria=models.CharField(max_length=40)
    subcategoria=models.CharField(max_length=40)

class Autores(models.Model):
    nombre=models.CharField(max_length=40)
    cantidadPosts=models.IntegerField()
    fecha_ingreso=models.DateField()
    mail = models.EmailField(max_length=200, blank=True, null=True)
