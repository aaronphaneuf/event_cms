from django.db import models
from core.models import Event

class CustomTicketFields(models.Model):
    name = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=255, blank=True)

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    custom_fields = models.ManyToManyField(CustomTicketFields, blank=True)
    name = models.CharField(max_length=255, blank=True)
    date = models.CharField(max_length=255, blank=True)
    time = models.CharField(max_length=255, blank=True)
    ticket_type = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    order_number = models.CharField(max_length=255, blank=True)
    custom_1 = models.CharField(max_length=255, blank=True)
    barcode = models.CharField(max_length=255, blank=True)

    text_field_1 = models.TextField(blank=True)
    text_field_2 = models.TextField(blank=True)
    text_field_3 = models.TextField(blank=True)
    text_field_4 = models.TextField(blank=True)
    text_field_5 = models.TextField(blank=True)
    text_field_6 = models.TextField(blank=True)
    text_field_7 = models.TextField(blank=True)
