from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    relacion = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre

