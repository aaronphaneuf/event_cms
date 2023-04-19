from django.db import models


class PriceType(models.Model):
    name = models.CharField(max_length=255) 

    # Shows the name on the admin page and on the serializer page
    def __str__(self) -> str:
        return self.name


class PriceLayer(models.Model):
    name = models.CharField(max_length=255)

    # Shows the name on the admin page and on the serializer page
    def __str__(self) -> str:
        return self.name
    

class Facility(models.Model): 
    facility_name = models.CharField(max_length=255)

    # Shows the name on the admin page and on the serializer page
    def __str__(self) -> str:
        return self.facility_name

    
class Event(models.Model):
    NORTH_ENTRANCE = 'N'
    SOUTH_ENTRANCE = 'S'
    WEST_ENTRANCE = 'W'

    ENTRANCE_CHOICES = [
        (NORTH_ENTRANCE, 'North'),
        (SOUTH_ENTRANCE, 'South'),
        (WEST_ENTRANCE, 'West')
    ]

    YES_CHOICE = 'Y'
    NO_CHOICE = 'N'

    YES_OR_NO_CHOICES = [
        (YES_CHOICE, 'Yes'),
        (NO_CHOICE, 'No')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    capacity = models.IntegerField()
    held = models.IntegerField()
    entrance = models.CharField(max_length=1, choices=ENTRANCE_CHOICES, default='NORTH_ENTRANCE')
    gr_required = models.CharField(max_length=1, choices=YES_OR_NO_CHOICES, default='NO_CHOICE')
    early_closure = models.CharField(max_length=1, choices=YES_OR_NO_CHOICES, default='NO_CHOICE')
    csi_needed = models.CharField(max_length=1, choices=YES_OR_NO_CHOICES, default='NO_CHOICE')
    csi_mandatory = models.CharField(max_length=1, choices=YES_OR_NO_CHOICES, default='NO_CHOICE')
    csi_notes = models.TextField()
    additional_notes = models.TextField()
    facility = models.ForeignKey(Facility, on_delete=models.PROTECT, null=True)
    price_type = models.ManyToManyField(PriceType)
    price_layer = models.ManyToManyField(PriceLayer)


class Location(models.Model): 
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    location_name = models.CharField(max_length=255)
    
    
class DateTime(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, primary_key=True, related_name='date_time') # related_name allows us to reference this in the reverse relationship.
    event_date = models.DateField(auto_now_add=False)
    event_time = models.TimeField()
    door_open = models.TimeField()
    door_close = models.TimeField()
    sell_date = models.DateField(auto_now_add=False)
    sell_time = models.TimeField()
    stop_date = models.DateTimeField(auto_now_add=False)
    stop_time = models.TimeField()
    early_closure_time = models.TimeField()


class TimeSlot(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    time_range = models.CharField(max_length=255)
    capacity = models.IntegerField()
    held = models.IntegerField()


class PriceLayerPrice(models.Model):
    price = models.IntegerField()
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='price_layer_price')
    price_type = models.ManyToManyField(PriceType)
    price_layer = models.ManyToManyField(PriceLayer)