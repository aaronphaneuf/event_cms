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
    
class Location(models.Model): 
    location_name = models.CharField(max_length=255)

    # Shows the name on the admin page and on the serializer page
    def __str__(self) -> str:
        return self.location_name

    
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

    STATUS_ON_SALE = 'OS'
    STATUS_PENDING = 'P'
    STATUS_SETUP = 'S'
    STATUS_ACTION_NEEDED = 'AN'
    STATUS_CONCLUDED = 'C'

    STATUS_CHOICES = [
        (STATUS_ON_SALE, 'On Sale'),
        (STATUS_PENDING, 'Pending'),
        (STATUS_SETUP, 'Setup'),
        (STATUS_ACTION_NEEDED, 'Action Needed'),
        (STATUS_CONCLUDED, 'Concluded')
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
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='STATUS_PENDING')
    website_link = models.CharField(max_length=255)
    websales_link = models.CharField(max_length=255)


class DateTime(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, primary_key=True, related_name='date_time') # related_name allows us to reference this in the reverse relationship.
    event_date = models.DateField(auto_now_add=False)
    event_time = models.TimeField()
    event_end_time = models.TimeField()
    door_open = models.TimeField()
    door_close = models.TimeField()
    sell_date = models.DateTimeField(auto_now_add=False)
    stop_date = models.DateTimeField(auto_now_add=False)
    early_closure_time = models.TimeField()


class TimeSlot(models.Model):
    TIME_RANGE_CHOICES = [
        ('6:00 - 6:30 AM', '0600'), ('6:30 - 7:00 AM', '0630')
    ]
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    time_range = models.CharField(max_length=14, choices=TIME_RANGE_CHOICES, default='6:00 - 6:30 AM')
    capacity = models.IntegerField()
    held = models.IntegerField()


class PriceLayerPrice(models.Model):
    price = models.IntegerField()
    event = models.ManyToManyField(Event, related_name='price_layer_price')
    price_type = models.ForeignKey(PriceType, on_delete=models.PROTECT)
    price_layer = models.ForeignKey(PriceLayer, on_delete=models.PROTECT)

class Price(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='prices')
    price_type = models.ForeignKey(PriceType, on_delete=models.PROTECT)
    price_1 = models.FloatField()
    price_2 = models.FloatField()
    price_3 = models.FloatField()
    price_4 = models.FloatField()
    price_5 = models.FloatField()
    price_6 = models.FloatField()

class GLAccount(models.Model):
    event = models.ManyToManyField(Event, related_name='gl_account')
    price_layer = models.ForeignKey(PriceLayer, on_delete=models.PROTECT)
    gl_account = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Discount(models.Model):
    event = models.ManyToManyField(Event, related_name='discount')
    price_type = models.ForeignKey(PriceType, on_delete=models.PROTECT)
    discount = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    