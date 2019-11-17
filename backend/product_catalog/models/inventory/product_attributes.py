from product_catalog.models.base import DomainEntity
from django.db import models


class ProductAttribute(DomainEntity):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    class Meta:
        app_label = 'product_catalog'
