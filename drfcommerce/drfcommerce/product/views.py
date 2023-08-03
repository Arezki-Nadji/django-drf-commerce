from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerialize
from drf_spectacular.utils import extend_schema


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerialize)
    def list(self, request):
        serializer = CategorySerialize(self.queryset, many=True)
        return Response(serializer.data)
