from django.db import models


class Person(models.Model):
    name_person = models.CharField(max_length=30)
    lastName_person = models.CharField(max_length=30)
    doc_DNI = models.CharField(max_length=15)
    country_person = models.CharField(max_length=15)
    departament_person = models.CharField(max_length=20)
    province_person = models.CharField(max_length=20)
    district_person = models.CharField(max_length=20)
    address_person = models.CharField(max_length=50)
    phone_person = models.CharField(max_length=15)
    mail_person = models.CharField(max_length=15)

    def __str__(self):
        return self.name_person
