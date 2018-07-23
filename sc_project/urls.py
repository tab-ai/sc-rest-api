from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bt.views import BandViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('bt', BandViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name='api')
]
