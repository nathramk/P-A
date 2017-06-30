from django.contrib import admin

from .models.categoria import Category
from .models.client import Client
from .models.detallePedido import DetailOrder
from .models.producto import Product
from .models.pedidos import Orders
from .models.person import Person


class AdminOrderDetail(admin.ModelAdmin):
    readonly_fields = ("name_detailOrder", "code_order", "code_product", "cant_order", "subtotal_order", "fecha_order")


# Register your models here.

admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Person)
admin.site.register(DetailOrder, AdminOrderDetail)
