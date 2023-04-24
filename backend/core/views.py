from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer, TimeSlotSerializer, DateTimeSerializer, SimpleEventSerializer, EditEventSerializer
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
