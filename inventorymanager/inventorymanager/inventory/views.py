from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Brand, Product, Stock, Supplier, IncomingOrder, OutgoingOrder
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer, StockSerializer, SupplierSerializer, IncomingOrderSerializer, OutgoingOrderSerializer


class CategoryView(viewsets.ViewSet):
    """
    The viewset for for viewing categories
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        """
        Return a list of all categories
        """
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        To create a new entry
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        """
        Updating the entry
        """
        category = self.queryset.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """
        Return a single entry
        """
        category = self.queryset.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def delete(self, request, pk=None):
        """
        Deleting the entry
        """
        category = self.queryset.get(pk=pk)
        category.delete()
        return Response(status=204)
    
class BrandView(viewsets.ViewSet):
    """
    The viewset for for viewing brands
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def list(self, request):
        """
        Return a list of all brands
        """
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        To create a new entry
        """
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def update(self, request, pk=None):
        """
        Updating the entry
        """
        category = self.queryset.get(pk=pk)
        serializer = BrandSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk=None):
        """
        Return a single entry
        """
        category = self.queryset.get(pk=pk)
        serializer = BrandSerializer(category)
        return Response(serializer.data)
    
class ProductView(viewsets.ViewSet):
    """
    The viewset for for viewing products
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        """
        Return a list of all products
        """
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """
        To create a new entry
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def update(self, request, pk=None):
        """
        Updating the entry
        """
        category = self.queryset.get(pk=pk)
        serializer = ProductSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk=None):
        """
        Return a single entry
        """
        category = self.queryset.get(pk=pk)
        serializer = ProductSerializer(category)
        return Response(serializer.data)
    

class StockView(viewsets.ViewSet):
    """
    For stock management
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def list(self, request):
        """
        Return a list of all stocks
        """
        serializer = StockSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """
        To create a new entry
        """
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def update(self, request, pk=None):
        """
        Updating the entry
        """
        category = self.queryset.get(pk=pk)
        serializer = StockSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk=None):
        """
        Return a single entry
        """
        category = self.queryset.get(pk=pk)
        serializer = StockSerializer(category)
        return Response(serializer.data)


class SupplierView(viewsets.ViewSet):
    """
    The viewset for for viewing suppliers
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def list(self, request):
        """
        Return a list of all suppliers
        """
        serializer = SupplierSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """
        To create a new entry
        """
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def update(self, request, pk=None):
        """
        Updating the entry
        """
        category = self.queryset.get(pk=pk)
        serializer = SupplierSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk=None):
        """
        Return a single entry
        """
        category = self.queryset.get(pk=pk)
        serializer = SupplierSerializer(category)
        return Response(serializer.data)


class IncomingOrderView(viewsets.ViewSet):
    """
    The viewset for for viewing incoming orders
    """
    queryset =IncomingOrder.objects.all()
    serializer_class =IncomingOrderSerializer

    def list(self, request):
        """
        Return a list of all incoming orders
        """
        serializer =IncomingOrderSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """
        To create a new entry
        """
        serializer =IncomingOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def update(self, request, pk=None):
        """
        Updating the entry
        """
        category = self.queryset.get(pk=pk)
        serializer =IncomingOrderSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk=None):
        """
        Return a single entry
        """
        category = self.queryset.get(pk=pk)
        serializer =IncomingOrderSerializer(category)
        return Response(serializer.data)


class OutgoingOrderView(viewsets.ViewSet):
    """
    The viewset for viewing outgoing orders
    """
    queryset = OutgoingOrder.objects.all()
    serializer_class = OutgoingOrderSerializer

    def list(self, request):
        """
        Return a list of all stocks
        """
        serializer = OutgoingOrderSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """
        To create a new entry
        """
        serializer = OutgoingOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def update(self, request, pk=None):
        """
        Updating the entry
        """
        category = self.queryset.get(pk=pk)
        serializer = OutgoingOrderSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def retrieve(self, request, pk=None):
        """
        Return a single entry
        """
        category = self.queryset.get(pk=pk)
        serializer = OutgoingOrderSerializer(category)
        return Response(serializer.data)
