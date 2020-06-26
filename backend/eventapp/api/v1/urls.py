from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import EventsViewSet, LocationsViewSet

router = DefaultRouter()
router.register("events", EventsViewSet)
router.register("locations", LocationsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
