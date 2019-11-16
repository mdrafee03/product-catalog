from rest_framework import serializers
from product_catalog.engine.serializer_fields.primary_key_related_fields import PrimaryKeyRelatedField
from product_catalog.models.base import DomainEntity

__author__ = 'Shohag'


class DomainEntitySerializer(serializers.ModelSerializer):
    serializer_related_field = PrimaryKeyRelatedField

    def __init__(self, *args, fields=None, context=None, **kwargs):
        super().__init__(*args, context=context, **kwargs)

    class Meta:
        model = DomainEntity
        read_only_fields = (
            'id', 'created_by', 'last_updated_by', 'date_created', 'last_updated', 'is_active',
            'is_deleted', 'is_locked', 'code'
        )
