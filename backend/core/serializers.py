from rest_framework import serializers
from .models import Event, TimeSlot, DateTime, Location, Facility, PriceType, PriceLayer, PriceLayerPrice

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

class TimeSlotSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeSlot
    fields = ['event', 'time_range', 'capacity', 'held']

class FacilitySerializer(serializers.ModelSerializer):
   class Meta:
      model = Facility
      fields = ['facility_name']


class DateTimeSerializer(serializers.ModelSerializer):
  class Meta:
    model = DateTime
    fields =  ['event', 'event_date' ,'event_time', 'event_end_time', 'door_open', 'door_close', 'sell_date', 'stop_date', 'early_closure_time', 'on_sale_date'
    ]
    read_only_fields = ['event']

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
  
  #all_facilities = FacilitySerializer(many=True, read_only=True, source="all_options")
  #facility = serializers.PrimaryKeyRelatedField(queryset=Facility.objects.all())
  facility = FacilitySerializer()
  location = LocationSerializer()
  price_type = PriceTypeSerializer(many=True, read_only=True)
  price_layer = PriceLayerSerializer(many=True, read_only=True)
  class Meta:
    model = Event
    
    fields = ['name', 'description', 'capacity', 'held', 'entrance', 'gr_required', 'early_closure', 'csi_needed', 'csi_mandatory', 'facility',
              'location', 'date_time', 'timeslot_set', 'price_type', 'price_layer', 'price_layer_price', 'status', 'website_link', 'websales_link',
              ]
    
  def create(self, validated_data):
        date_data = validated_data.pop('date_time')
        event = Event.objects.create(**validated_data)
        # The event must be created first since the foreign key lives on the DateTime model. We need an event to insert. 
        DateTime.objects.create(event=event, **date_data)
        
        return event

class SimpleDateTimeSerializer(serializers.ModelSerializer):
  class Meta:
    model = DateTime
    fields =  ['event_date']

class SimpleEventSerializer(serializers.ModelSerializer):
  date_time = SimpleDateTimeSerializer()
  class Meta:
    model = Event
    fields = ['id', 'name', 'date_time']
