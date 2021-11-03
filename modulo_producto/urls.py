from django.urls import path
from . import views

app_name = "predict"

urlpatterns = [
    path('', views.insertar, name='insertar'),
    path('listar/', views.listar, name='listar'),
    path('<id>', views.editar, name='editar'),
    path('aliminar/<id>', views.eliminar, name='eliminar'),
]