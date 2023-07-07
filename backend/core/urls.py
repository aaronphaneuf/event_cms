from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet, basename='events')
router.register(r'simple_events', views.SimpleEventViewSet, basename='simple_events')
router.register(r'editevent', views.EditEventViewSet, basename='editevent')
router.register(r'addevent', views.AddEventViewSet, basename='addevent')
router.register(r'facility', views.FacilityViewSet, basename='facility')
router.register(r'location', views.LocationViewSet, basename='location')
router.register(r'pricetype', views.PriceTypeViewSet, basename='pricetype')
router.register(r'pricelayer', views.PriceLayerViewSet, basename='pricelayer')
router.register(r'account', views.AccountViewSet, basename='account')


urlpatterns = [ 
    path("", include(router.urls)),
]
