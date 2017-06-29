from django.db import models
from .pedidos import Orders
from .producto import Product


class DetailOrder(models.Model):
    name_detailOrder = models.CharField(max_length=20)
    code_order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    code_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cant_order = models.IntegerField()  # ,
    subtotal_order = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.code_order, self.cant_order)
