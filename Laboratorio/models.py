from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(validators=[
        MinValueValidator('2015-01-01'),
        MaxValueValidator('2023-07-17')
    ])
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)
