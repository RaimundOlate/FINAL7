from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto
# Register your models here.


@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    ordering = ['nombre']


@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    ordering = ['nombre']

    class Meta:
        verbose_name = 'Director General'
        verbose_name_plural = 'Directores Generales'


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio',
                    'f_fabricacion', 'p_costo', 'p_venta')
    ordering = ['nombre', 'laboratorio']

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
