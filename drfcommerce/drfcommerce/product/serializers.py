from rest_framework import serializers

from .models import Brand, Category, Product


class CategorySerialize(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandCategory(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductCategory(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
