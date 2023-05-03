from django.db import models

# Create your models here.


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    nacionalidad = models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_libro = models.CharField(max_length=200, blank=False, null=False)
    agno_publicacion = models.DateField()