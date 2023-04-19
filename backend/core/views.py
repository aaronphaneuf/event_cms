from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer, TimeSlotSerializer, DateTimeSerializer, SimpleEventSerializer
from rest_framework import viewsets

class EventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

class SimpleEventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = SimpleEventSerializer
