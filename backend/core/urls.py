from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet, basename='events')
router.register(r'simple_events', views.SimpleEventViewSet, basename='simple_events')
router.register(r'editevent', views.EditEventViewSet, basename='editevent')


urlpatterns = [ 
    path("", include(router.urls)),
]