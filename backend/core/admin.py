from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Event)
admin.site.register(models.DateTime)
admin.site.register(models.TimeSlot)
admin.site.register(models.Location)
admin.site.register(models.PriceLayer)
admin.site.register(models.PriceType)
admin.site.register(models.PriceLayerPrice)
admin.site.register(models.Facility)
admin.site.register(models.Discount)
admin.site.register(models.Price)
admin.site.register(models.Account)
admin.site.register(models.AccountLayer)

admin.site.register(models.ChangeLog)