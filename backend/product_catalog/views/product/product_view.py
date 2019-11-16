from rest_framework import viewsets
from rest_framework.response import Response
from product_catalog.models import Product
from product_catalog.serializers.product.product_serializer import ProductSerializer


class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
