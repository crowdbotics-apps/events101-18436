from rest_framework import authentication
from eventapp.models import Events, Locations
from .serializers import EventsSerializer, LocationsSerializer
from rest_framework import viewsets


class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Events.objects.all()


class LocationsViewSet(viewsets.ModelViewSet):
    serializer_class = LocationsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Locations.objects.all()
