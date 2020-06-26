from rest_framework import serializers
from eventapp.models import Events, Locations


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = "__all__"
