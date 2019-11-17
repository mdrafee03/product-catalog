from product_catalog.models import Product
from product_catalog.serializers.domain_entity_serializer import DomainEntitySerializer

__author__ = 'Shohag'


class ProductSerializer(DomainEntitySerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'name', 'code', 'translated_name', 'description', 'translated_description', 'unit', 'sku', 'price',
            'attributes', 'slug')
