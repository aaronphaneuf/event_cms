from django.urls import include, path
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'ticket', views.TicketViewSet, basename='ticket')

urlpatterns = [
        path("", include(router.urls)),
        path('ticket_view/<int:pk>', views.TicketPDFView.as_view(), name='ticket_view'),
        path('ticket_detail/<int:pk>', views.TicketDetailView.as_view(), name='ticket_detail'),
     ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
