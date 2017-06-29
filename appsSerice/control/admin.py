from django.contrib import admin

from .models.categoria import Category
from .models.client import Client
from .models.detallePedido import DetailOrder
from .models.producto import Product
from .models.pedidos import Orders
from .models.person import Person

# Register your models here.

admin.site.register(Category)
admin.site.register(Client)
admin.site.register(DetailOrder)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Person)