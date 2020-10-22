from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .views import PersonViewSet

router = routers.DefaultRouter()
router.register(r'employee', PersonViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]