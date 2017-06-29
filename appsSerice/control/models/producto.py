from django.db import models
from django.core.urlresolvers import reverse
from .categoria import Category
from datetime import datetime


class Product(models.Model):
    cod_product = models.CharField(max_length=50)
    nome_product = models.CharField(max_length=50)
    marca_product = models.CharField(max_length=50)
    cant_product = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    fecha_ingreso = models.DateField(blank=False, default=datetime.now())
    product_logo = models.FileField()

    def __str__(self):
        return self.cod_product
