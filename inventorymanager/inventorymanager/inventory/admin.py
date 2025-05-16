from django.contrib import admin
from .models import Brand, Category, Product, Stock, Supplier, IncomingOrder, OutgoingOrder

# Register your models here.
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Supplier)
admin.site.register(IncomingOrder)
admin.site.register(OutgoingOrder)