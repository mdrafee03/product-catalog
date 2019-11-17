# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-17 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog', '0002_auto_20191116_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.BigIntegerField(default=0, editable=False)),
                ('last_updated', models.BigIntegerField(default=0, editable=False)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('is_locked', models.BooleanField(default=False, editable=False)),
                ('code', models.CharField(default='', max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='product_catalog.ConsoleUser')),
                ('last_updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='product_catalog.ConsoleUser')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.ManyToManyField(related_name='attribute', to='product_catalog.ProductAttribute'),
        ),
    ]
