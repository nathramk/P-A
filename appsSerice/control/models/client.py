from django.db import models
from .person import Person


class Client(models.Model):
    client_code = models.CharField(max_length=50)
    client_person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_code
