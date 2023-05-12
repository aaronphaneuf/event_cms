from django.shortcuts import render
from .models import Event, Facility, Location, PriceType, PriceLayerPrice, Account
from .serializers import *
from rest_framework import viewsets

class EventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

class EditEventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = EditEventSerializer

class SimpleEventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = SimpleEventSerializer

class FacilityViewSet(viewsets.ModelViewSet):
  queryset = Facility.objects.all()
  serializer_class = FacilitySerializer

class LocationViewSet(viewsets.ModelViewSet):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

class PriceTypeViewSet(viewsets.ModelViewSet):
  queryset = PriceType.objects.all()
  serializer_class = PriceTypeSerializer

class PriceLayerViewSet(viewsets.ModelViewSet):
  queryset = PriceLayer.objects.all()
  serializer_class = PriceLayerSerializer

class PriceLayerPriceViewSet(viewsets.ModelViewSet):
  queryset = PriceLayerPrice.objects.all()
  serializer_class = PriceLayerPriceSerializer

class AccountViewSet(viewsets.ModelViewSet):
  queryset = Account.objects.all()
  serializer_class = AccountSerializer
