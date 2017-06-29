from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from appsSerice.control.models.categoria import Category
from appsSerice.control.models.producto import Product


class ProductCreate(CreateView):
    model = Product
    template_name = ['cod_product',
                     'nome_product',
                     'marca_product',
                     'cant_product',
                     'category',
                     'precio_unitario',
                     'fecha_ingreso',
                     'product_logo']


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('control:detail')
