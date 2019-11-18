from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from product_catalog.models import Product
from product_catalog.serializers.product.product_serializer import ProductSerializer
from product_catalog.serializers.product.product_serializer import ProductPriceSerializer
from product_catalog.serializers.product.product_serializer import ProductAttributeSerializer


class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def prices(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

        serializer = ProductPriceSerializer(data=request.data)
        if serializer.is_valid():
            productprice = serializer.save()
            product.price.add(productprice)
            serializerProduct = ProductSerializer(product)
            return Response(serializerProduct.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def attributes(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

        serializer = ProductAttributeSerializer(data=request.data)
        if serializer.is_valid():
            productAttribute = serializer.save()
            product.attributes.add(productAttribute)
            serializerProduct = ProductSerializer(product)
            return Response(serializerProduct.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
