from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'product_types'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, blank=True, unique=True)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=True)
    type = models.ForeignKey(Type, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'products'

    @property
    def image_url(self):
        return settings.MEDIA_URL + str(self.image)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Product)
def set_slug_on_pre_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
