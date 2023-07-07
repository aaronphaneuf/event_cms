from django.contrib import admin
from django.urls import path
from django.urls import include # This must be included in your existing import statements

urlpatterns = [
  path("", include('core.urls')),
  path("admin/", admin.site.urls),
  path('api/v1/', include('djoser.urls')),
  path('api/v1/', include('djoser.urls.authtoken')),
  path('api/v1/', include('core.urls')),
  path('api/v1/', include('ticket.urls')),

]
