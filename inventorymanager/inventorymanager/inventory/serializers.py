from rest_framework import serializers
from .models import Brand, Category, Product, Stock, Supplier, IncomingOrder, OutgoingOrder

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'brand', 'price', 'description', 'image', 'created_at', 'updated_at']

class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Stock
        fields = ['id', 'product', 'quantity', 'productPrice', 'totalPrice', 'created_at', 'updated_at']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'created_at']

class IncomingOrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    status = serializers.ChoiceField(choices=IncomingOrder.STATUS_CHOICES)
    class Meta:
        model = IncomingOrder
        fields = ['id', 'status', 'supplierId', 'product', 'quantity', 'price', 'created_at']

class OutgoingOrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    status = serializers.ChoiceField(choices=OutgoingOrder.STATUS_CHOICES)
    class Meta:
        model = OutgoingOrder
        fields = ['id', 'status', 'product', 'quantity', 'price', 'created_at']