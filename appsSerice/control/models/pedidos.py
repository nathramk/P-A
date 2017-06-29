from django.db import models
from .client import Client


class Orders(models.Model):
    code_order = models.CharField(max_length=20)
    code_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_order = models.CharField(max_length=20)
    status_order = models.BooleanField(default=False)
    message_order = models.CharField(max_length=150)

    def __str__(self):
        return self.code_order  # + ' - ' + self.code_client
