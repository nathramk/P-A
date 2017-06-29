from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    user = models.ForeignKey(User, default=1)
    name_category = models.CharField(max_length=50)
    category_logo = models.FileField()

    def __str__(self):
        return self.name_category

    #     def get_absolute_url(self):
    #    return reverse('control:detail', kwargs={'pk': self.pk})
