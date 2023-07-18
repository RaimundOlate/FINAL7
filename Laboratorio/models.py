from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date


class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255, null=True, blank=True)
    pais = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(validators=[
        MinValueValidator(date(2015, 1, 1)),
        MaxValueValidator(date(2023, 7, 17))
    ])
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
