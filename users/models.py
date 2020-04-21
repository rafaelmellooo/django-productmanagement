from django.db import models

from products.models import Product


class User(models.Model):
    name = models.CharField(max_length=80, unique=True)
    products = models.ManyToManyField(Product, blank=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name
