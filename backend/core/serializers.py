from rest_framework import serializers
from .models import Event, TimeSlot, DateTime, Location, Facility, PriceType, PriceLayer, PriceLayerPrice

class PriceLayerPriceSerializer(serializers.ModelSerializer):
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
    fields =  ['event', 'event_date' ,'event_time', 'door_open', 'door_close', 'sell_date', 'sell_time', 'stop_date', 'stop_time', 'early_closure_time'
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
  price_layer_price = PriceLayerPriceSerializer()
  
  #all_facilities = FacilitySerializer(many=True, read_only=True, source="all_options")
  facility = serializers.PrimaryKeyRelatedField(queryset=Facility.objects.all())
  price_type = PriceTypeSerializer(many=True, read_only=True)
  price_layer = PriceLayerSerializer(many=True, read_only=True)
  class Meta:
    model = Event
    
    fields = ['name', 'description', 'capacity', 'held', 'entrance', 'gr_required', 'early_closure', 'csi_needed', 'csi_mandatory', 'facility',
              'date_time', 'timeslot_set', 'price_type', 'price_layer', 'price_layer_price']#'location_set', 'facility'] #'timeslot_set',]
    
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
