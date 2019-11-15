from product_catalog.models.base import DomainEntity
from django.db import models

__author__ = 'Fazlul Kabir Shohag'


class Product(DomainEntity):
    name = models.CharField(max_length=500)
    translated_name = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=8000, blank=True)
    translated_description = models.CharField(max_length=8000, blank=True)
    unit = models.CharField(max_length=1024, blank=True)
    sku = models.CharField(max_length=100, blank=True)
    price = models.ManyToManyField('product_catalog.ProductPrice', related_name="+")
    slug = models.SlugField(unique=True, max_length=100)

    class Meta:
        app_label = 'product_catalog'

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
