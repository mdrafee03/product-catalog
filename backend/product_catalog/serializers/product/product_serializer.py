from product_catalog.models import Product
from product_catalog.serializers.domain_entity_serializer import DomainEntitySerializer
from product_catalog.serializers.product.product_attributes_serializer import ProductAttributeSerializer

__author__ = 'Shohag'


class ProductSerializer(DomainEntitySerializer):
    attributes = ProductAttributeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'translated_name', 'description', 'translated_description', 'unit', 'sku', 'price',
            'attributes', 'slug')
