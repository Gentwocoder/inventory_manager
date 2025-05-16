from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Stock, IncomingOrder, OutgoingOrder

@receiver(pre_save, sender=IncomingOrder)
def update_stock_on_incoming_order(sender, instance, **kwargs):
    if instance.status == 'received':
        stock = Stock.objects.get(id=instance.stock_id)
        stock.quantity += instance.quantity
        stock.save()

@receiver(pre_save, sender=OutgoingOrder)
def update_stock_on_outgoing_order(sender, instance, **kwargs):
    if instance.status == 'delivered':
        stock = Stock.objects.get(id=instance.stock_id)
        stock.quantity -= instance.quantity
        stock.save()