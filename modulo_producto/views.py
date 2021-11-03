from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from modulo_producto.forms import Productos
from .models import Producto

def insertar(request):
    context = {}
 
    form = Productos(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form']= form

    return render(request, "index.html", context)


def listar(request):
    context = {}
 
    context["dataset"] = Producto.objects.all()
         
    return render(request, "listar.html", context)


def editar(request, id):
    context = {}
 
    obj = get_object_or_404(Producto, id = id)
 
    form = Productos(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
 
    context["form"] = form
 
    return render(request, "actualizar.html", context)


def eliminar(request, id):
    context = {}
 
    obj = get_object_or_404(Producto, id = id)
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/listar")
 
    return render(request, "listar.html", context)