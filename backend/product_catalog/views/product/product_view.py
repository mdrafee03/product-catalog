from django.shortcuts import get_object_or_404
from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from product_catalog.models import Product
from product_catalog.serializers.product.product_serializer import ProductSerializer


class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def attributes(self, request, pk=None):
        name = request.data.get('name')
        value = request.data.get('value')
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        product.attributes.create(name=name, value=value)
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
