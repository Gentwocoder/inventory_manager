from rest_framework import serializers
from .models import Brand, Category, Product, Stock, Supplier, IncomingOrder, OutgoingOrder

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class IncomingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingOrder
        fields = '__all__'

class OutgoingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutgoingOrder
        fields = '__all__'