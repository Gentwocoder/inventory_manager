from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Category(MPTTModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, unique=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    brandId = models.ForeignKey(Brand, on_delete=models.CASCADE)
    categoryId = TreeForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.productId.name} Stock"

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class IncomingOrder(models.Model):
    id = models.AutoField(primary_key=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    supplierId = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Incoming {self.productId.name} from {self.supplierId.first_name} {self.supplierId.last_name}"

class OutgoingOrder(models.Model):
    id = models.AutoField(primary_key=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Outgoing {self.productId.name}"
