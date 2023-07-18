from django.urls import path
from . import views

urlpatterns = [
    path('', views.laboratorio_lista, name='laboratorio_lista'),
    path('insertar/', views.laboratorio_insertar, name='laboratorio_insertar'),
    path('<int:laboratorio_id>/', views.laboratorio_detalle,
         name='laboratorio_detalle'),
    path('<int:laboratorio_id>/actualizar/',
         views.laboratorio_actualizar, name='laboratorio_actualizar'),
    path('<int:laboratorio_id>/borrar/',
         views.laboratorio_borrar, name='laboratorio_borrar'),
]
