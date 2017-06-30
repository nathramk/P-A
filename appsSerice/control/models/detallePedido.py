from django.db import models
from .pedidos import Orders
from .producto import Product
from datetime import datetime


class DetailOrder(models.Model):
    name_detailOrder = models.CharField(max_length=20)
    code_order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    code_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cant_order = models.IntegerField()
    subtotal_order = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    fecha_order = models.DateField(blank=False, default=datetime.now())

    def __unicode__(self):
        return u'%s %s' % (self.name_detailOrder, self.code_order)
