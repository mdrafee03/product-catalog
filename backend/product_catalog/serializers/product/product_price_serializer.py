from product_catalog.models import ProductPrice
from product_catalog.serializers.domain_entity_serializer import DomainEntitySerializer

__author__ = 'Shohag'


class ProductPriceSerializer(DomainEntitySerializer):
    class Meta:
        model = ProductPrice
        fields = (
            'id', 'value', 'active_from', 'active_upto')
