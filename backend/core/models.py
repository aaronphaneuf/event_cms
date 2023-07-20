from django.db import models


class PriceType(models.Model):
    name = models.CharField(max_length=255, unique=True) 

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
    NORTH_ENTRANCE = 'North Entrance'
    SOUTH_ENTRANCE = 'South Entrance'
    WEST_ENTRANCE = 'West Entrance'

    ENTRANCE_CHOICES = [
        (NORTH_ENTRANCE, 'North'),
        (SOUTH_ENTRANCE, 'South'),
        (WEST_ENTRANCE, 'West')
    ]

    YES_CHOICE = 'Yes'
    NO_CHOICE = 'No'

    YES_OR_NO_CHOICES = [
        (YES_CHOICE, 'Y'),
        (NO_CHOICE, 'N')
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
    entrance = models.CharField(max_length=14, choices=ENTRANCE_CHOICES, default='NORTH_ENTRANCE')
    gr_required = models.CharField(max_length=3, choices=YES_OR_NO_CHOICES, default='NO_CHOICE')
    early_closure = models.CharField(max_length=3, choices=YES_OR_NO_CHOICES, default='NO_CHOICE')
    csi_needed = models.CharField(max_length=3, choices=YES_OR_NO_CHOICES, default='NO_CHOICE')
    csi_mandatory = models.CharField(max_length=3, choices=YES_OR_NO_CHOICES, default='NO_CHOICE')
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
    TIME_RANGE_CHOICES = [    ('6:00 - 6:30 AM', '0600'),    ('6:30 - 7:00 AM', '0630'),    ('7:00 - 7:30 AM', '0700'),    ('7:30 - 8:00 AM', '0730'),    ('8:00 - 8:30 AM', '0800'),    ('8:30 - 9:00 AM', '0830'),    ('9:00 - 9:30 AM', '0900'),    ('9:30 - 10:00 AM', '0930'),    ('10:00 - 10:30 AM', '1000'),    ('10:30 - 11:00 AM', '1030'),    ('11:00 - 11:30 AM', '1100'),    ('11:30 - 12:00 PM', '1130'),    ('12:00 - 12:30 PM', '1200'),    ('12:30 - 1:00 PM', '1230'),    ('1:00 - 1:30 PM', '1300'),    ('1:30 - 2:00 PM', '1330'),    ('2:00 - 2:30 PM', '1400'),    ('2:30 - 3:00 PM', '1430'),    ('3:00 - 3:30 PM', '1500'),    ('3:30 - 4:00 PM', '1530'),    ('4:00 - 4:30 PM', '1600'),    ('4:30 - 5:00 PM', '1630'),    ('5:00 - 5:30 PM', '1700'),    ('5:30 - 6:00 PM', '1730'),    ('6:00 - 6:30 PM', '1800'),    ('6:30 - 7:00 PM', '1830'),    ('7:00 - 7:30 PM', '1900'),    ('7:30 - 8:00 PM', '1930'),    ('8:00 - 8:30 PM', '2000'),    ('8:30 - 9:00 PM', '2030'),    ('9:00 - 9:30 PM', '2100'),    ('9:30 - 10:00 PM', '2130'),    ('10:00 - 10:30 PM', '2200'),    ('10:30 - 11:00 PM', '2230'),    ('11:00 - 11:30 PM', '2300'),    ('11:30 - 12:00 AM', '2330'),    ('12:00 - 12:30 AM', '2400')]

    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    time_range = models.CharField(max_length=16, choices=TIME_RANGE_CHOICES, default='6:00 - 6:30 AM')
    capacity = models.IntegerField()
    held = models.IntegerField()


class PriceLayerPrice(models.Model):
    price = price = models.DecimalField(max_digits=5, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='price_layer_price')
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


class Account(models.Model):
    gl_account = models.CharField(max_length=255)
 

class Discount(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='discount')
    price_type = models.ForeignKey(PriceType, on_delete=models.PROTECT)
    discount = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class AccountLayer(models.Model):
    gl_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    event = models.ManyToManyField(Event, related_name='account')
    price_layer = models.ForeignKey(PriceLayer, on_delete=models.CASCADE)
