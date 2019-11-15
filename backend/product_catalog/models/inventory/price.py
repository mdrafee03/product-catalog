from product_catalog.models.base import DomainEntity
from django.db import models
import sys


class ProductPrice(DomainEntity):
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    active_from = models.BigIntegerField(default=0)
    active_upto = models.BigIntegerField(default=sys.maxsize)

    class Meta:
        app_label = 'product_catalog'
