from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto
# Register your models here.


@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    pass


@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Director General'
        verbose_name_plural = 'Directores Generales'


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
