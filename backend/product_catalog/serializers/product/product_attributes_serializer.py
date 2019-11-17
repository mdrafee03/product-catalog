from product_catalog.models import  ProductAttribute
from product_catalog.serializers.domain_entity_serializer import DomainEntitySerializer

__author__ = 'Shohag'


class ProductAttributeSerializer(DomainEntitySerializer):
    class Meta:
        model = ProductAttribute
        fields = (
            'id', 'name', 'value')
