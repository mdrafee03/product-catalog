from product_catalog.models.base import DomainEntity
from django.contrib.auth.models import User
from product_catalog.models.email.emailaddress import EmailAddress
from django.db import models

__author__ = 'Fazlul Kabir Shohag'


class ConsoleUser(DomainEntity):
    user = models.OneToOneField(User, null=True)
    is_super = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    email_address = models.ForeignKey(EmailAddress, null=True, on_delete=models.SET_NULL)
    designation = models.CharField(max_length=200, null=True)
    male_or_female = models.CharField(max_length=2, null=True, default='M',
                                      blank=True)
    is_first_login = models.BooleanField(default=True)

    class Meta:
        app_label = 'product_catalog'

    def __init__(self, *args, **kwargs):
        super(ConsoleUser, self).__init__(*args, **kwargs)
