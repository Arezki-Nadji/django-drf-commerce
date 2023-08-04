from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSeriliazer, ProductSerializer
from drf_spectacular.utils import extend_schema


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing brands
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = BrandSeriliazer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing Products
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
