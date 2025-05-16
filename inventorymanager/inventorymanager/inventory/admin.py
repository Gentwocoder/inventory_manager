from django.contrib import admin
from .models import Brand, Category, Product, Stock, Supplier, IncomingOrder, OutgoingOrder

# Register your models here.
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Supplier)
# admin.site.register(IncomingOrder)
admin.site.register(OutgoingOrder)

@admin.register(IncomingOrder)
class IncomingOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'productId', 'supplierId', 'quantity', 'price', 'created_at')
    list_filter = ('status', 'productId', 'supplierId')


class OutgoingOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'productId', 'quantity', 'price', 'created_at')
    list_filter = ('status', 'productId')