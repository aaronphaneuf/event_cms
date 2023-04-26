from django.shortcuts import render
from .models import Event, Facility, Location
from .serializers import EventSerializer, TimeSlotSerializer, DateTimeSerializer, SimpleEventSerializer, EditEventSerializer, FacilitySerializer, LocationSerializer
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
