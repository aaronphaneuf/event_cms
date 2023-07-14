from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event
from ticket.models import Ticket

@receiver(post_save, sender=Event)
def create_ticket(sender, instance, created, **kwargs):
    if created:
        Ticket.objects.create(event=instance)
