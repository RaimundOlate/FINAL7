from django.shortcuts import render, get_object_or_404, redirect
from .models import Laboratorio
from .forms import LaboratorioForm


def laboratorio_mostrar(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio_mostrar.html', {'laboratorios': laboratorios})


def laboratorio_detalle(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    return render(request, 'laboratorio_detalle.html', {'laboratorio': laboratorio})


def laboratorio_insertar(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_mostrar')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio_insertar.html', {'form': form})


def laboratorio_actualizar(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_mostrar')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio_actualizar.html', {'form': form, 'laboratorio': laboratorio})


def laboratorio_borrar(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio_mostrar')
    return render(request, 'laboratorio_borrar.html', {'laboratorio': laboratorio})
