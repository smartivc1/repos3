
from django import forms
from .models import Producto
 
 
class Productos(forms.ModelForm):

    class Meta:
        # specify model to be used
        model = Producto
 
        # specify fields to be used
        fields = [
            "user",
            "nombreProducto",
            "stockInicial",
            "stockActual",
            "precio",
            "estado"
        ]