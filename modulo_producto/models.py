from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Producto(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=CASCADE)
    nombreProducto = models.CharField("Nombre del producto", max_length=30, blank=False)
    stockInicial = models.IntegerField("Stock inicial", blank=False)
    stockActual = models.IntegerField("Stock Actual", blank=False)
    precio = models.IntegerField("precio del producto", blank=False)
    estado = models.BooleanField("estado del producto", blank=False)
    createDate = models.DateTimeField("Fecha de creacion", auto_now_add=True, blank=False)
    updateDate = models.DateTimeField("Fecha de modificacion", auto_now=True, blank=False)

    class Meta:
        verbose_name_plural = "Productos"

    def __str__(self):
        return str(self.nombreProducto)