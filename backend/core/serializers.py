from rest_framework import serializers, generics
from .models import *
from datetime import datetime

class DiscountSerializer(serializers.ModelSerializer):
  price_type = serializers.StringRelatedField()
  class Meta:
    model = Discount
    fields = ['price_type', 'discount', 'description']

class GLAccountSerializer(serializers.ModelSerializer):
  price_layer = serializers.StringRelatedField()
  class Meta:
    model = GLAccount
    fields = ['price_layer', 'gl_account', 'description']

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = ['location_name']

class PriceLayerPriceSerializer(serializers.ModelSerializer):
  price_type = serializers.StringRelatedField()
  price_layer = serializers.StringRelatedField()
  class Meta:
    model = PriceLayerPrice
    fields = ['price_type', 'price_layer', 'price']

class PriceSerializer(serializers.ModelSerializer):
  price_type = serializers.StringRelatedField()
  class Meta:
    model = Price
    fields =  ['price_type', 'price_1', 'price_2', 'price_3', 'price_4', 'price_5', 'price_6']

class TimeSlotSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeSlot
    fields = ['event', 'time_range', 'capacity', 'held']

class FacilitySerializer(serializers.ModelSerializer):
   class Meta:
      model = Facility
      fields = ['facility_name']



class DateTimeSerializer(serializers.ModelSerializer):
  event = serializers.PrimaryKeyRelatedField(read_only=True)
  event_date = serializers.DateField()
  event_time = serializers.TimeField()
  event_end_time = serializers.TimeField()
  door_open = serializers.TimeField()
  door_close = serializers.TimeField()
  sell_date = serializers.DateTimeField()
  stop_date = serializers.DateTimeField()
  early_closure_time = serializers.TimeField()

  def to_representation(self, instance):
        # Convert datetime object to a string in the format 'YYYY-MM-DD'
        event_date = instance.event_date.strftime('%Y-%m-%d')
        event_time = instance.event_time.strftime('%H:%M')
        event_end_time = instance.event_end_time.strftime('%H:%M')
        door_open = instance.door_open.strftime('%H:%M')
        door_close = instance.door_close.strftime('%H:%M')
        sell_date = instance.sell_date.strftime('%Y-%m-%d %H:%M')
        stop_date = instance.stop_date.strftime('%Y-%m-%d %H:%M')
        early_closure_time = instance.early_closure_time.strftime('%H:%M')

        return {
            'event': instance.event.id,
            'event_date': event_date,
            'event_time': event_time,
            'event_end_time': event_end_time,
            'door_open': door_open,
            'door_close': door_close,
            'sell_date': sell_date,
            'stop_date': stop_date,
            'early_closure_time': early_closure_time,
        }

  

  class Meta:
    model = DateTime
    fields =  ['event', 'event_date' ,'event_time', 'event_end_time', 'door_open', 'door_close', 'sell_date', 'stop_date', 'early_closure_time'
    ]
   

class PriceTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = PriceType
    fields =  ['name']

class PriceLayerSerializer(serializers.ModelSerializer):
  class Meta:
    model = PriceLayer
    fields =  ['name']

  
    
    
class EventSerializer(serializers.ModelSerializer):
  timeslot_set = TimeSlotSerializer(many=True, read_only=True)
  date_time = DateTimeSerializer()
  price_layer_price = PriceLayerPriceSerializer(many=True, read_only=True)
  gl_account = GLAccountSerializer(many=True, read_only=True)
  discount = DiscountSerializer(many=True, read_only=True)
  prices = PriceSerializer(many=True)
  
  #all_facilities = FacilitySerializer(many=True, read_only=True, source="all_options")
  #facility = serializers.PrimaryKeyRelatedField(queryset=Facility.objects.all())
  facility = FacilitySerializer()
  location = LocationSerializer()
  price_type = PriceTypeSerializer(many=True, read_only=True)
  price_layer = PriceLayerSerializer(many=True, read_only=True)
  class Meta:
    model = Event
    
    fields = ['id', 'name', 'description', 'capacity', 'held', 'entrance', 'gr_required', 'early_closure', 'csi_needed', 'csi_mandatory', 'csi_notes', 'facility',
              'location', 'date_time', 'timeslot_set', 'price_type', 'price_layer', 'price_layer_price', 'status', 'website_link', 'websales_link',
              'gl_account', 'discount', 'additional_notes', 'prices']
    
  def create(self, validated_data):
        date_data = validated_data.pop('date_time')
        event = Event.objects.create(**validated_data)
        # The event must be created first since the foreign key lives on the DateTime model. We need an event to insert. 
        DateTime.objects.create(event=event, **date_data)
        
        return event
  

class EditEventSerializer(serializers.ModelSerializer):
  timeslot_set = TimeSlotSerializer(many=True)
  date_time = DateTimeSerializer()
  price_layer_price = PriceLayerPriceSerializer(many=True, read_only=True)
  gl_account = GLAccountSerializer(many=True, read_only=True)
  discount = DiscountSerializer(many=True, read_only=True)
  
  
  price_type = PriceTypeSerializer(many=True, read_only=True)
  price_layer = PriceLayerSerializer(many=True, read_only=True)

  location = serializers.CharField(source='location.location_name')
  facility = serializers.CharField(source='facility.facility_name')
 
  class Meta:
    model = Event
    
    
    fields = ['id', 'name', 'description', 'capacity', 'held', 'entrance', 'gr_required', 'early_closure', 'csi_needed', 'csi_mandatory', 'csi_notes', 
              'location', 'date_time', 'timeslot_set', 'price_type', 'price_layer', 'price_layer_price', 'status', 'website_link', 'websales_link', 'facility',
              'gl_account', 'discount', 'additional_notes']
    
    
  def create(self, validated_data):
        date_data = validated_data.pop('date_time')
        event = Event.objects.create(**validated_data)
        # The event must be created first since the foreign key lives on the DateTime model. We need an event to insert. 
        DateTime.objects.create(event=event, **date_data)
        return event
  

  def get_date_time(self, obj):
        return {'event_date': obj.date_time.strftime('%Y-%m-%d %H:%M:%S')}

  def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.held = validated_data.get('held', instance.held)
        instance.entrance = validated_data.get('entrance', instance.entrance)
        instance.gr_required = validated_data.get('gr_required', instance.gr_required)
        instance.early_closure = validated_data.get('early_closure', instance.early_closure)
        #instance.date_time = validated_data.get('date_time', instance.date_time)
        location_name = validated_data.get('location', {}).get('location_name')
        
        if location_name:
            location, _ = Location.objects.get_or_create(location_name=location_name)
            instance.location = location
        facility_name = validated_data.get('facility', {}).get('facility_name')
        if facility_name:
            facility, _ = Facility.objects.get_or_create(facility_name=facility_name)
            instance.facility = facility
        instance.save()

        # Update the DateTime model
        date_time_data = validated_data.get('date_time')
        if date_time_data:
            date_time_fields = ['event_date', 'event_time', 'event_end_time',
                                'sell_date', 'stop_date', 'door_open',
                                'door_close', 'early_closure_time']
            for field_name in date_time_fields:
                field_value = date_time_data.get(field_name)
                if field_value is not None:
                    setattr(instance.date_time, field_name, field_value)
            instance.date_time.save()

        # Update the TimeSlot model
        timeslot_set_data = validated_data.get('timeslot_set')
        if timeslot_set_data:
            for timeslot_data in timeslot_set_data:
                time_range = timeslot_data['time_range']
                try:
                    # Try to get an existing TimeSlot object with the same time_range
                    timeslot = instance.timeslot_set.get(time_range=time_range)
                except TimeSlot.DoesNotExist:
                    # If no existing object was found, create a new one
                    timeslot = TimeSlot(event=instance, time_range=time_range)
                # Update the capacity and held fields of the TimeSlot object
                timeslot.capacity = timeslot_data['capacity']
                timeslot.held = timeslot_data['held']
                timeslot.save()

        return instance
  

class SimpleDateTimeSerializer(serializers.ModelSerializer):
  class Meta:
    model = DateTime
    fields =  ['event', 'event_date']

class SimpleEventSerializer(serializers.ModelSerializer):
  date_time = SimpleDateTimeSerializer()
  class Meta:
    model = Event
    fields = ['id', 'name', 'date_time']



