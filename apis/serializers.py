from rest_framework import serializers
from flight.models import *


class Passenger(serializers.ModelSerializer):
    class Meta:
        fields = (
            'first',
            'last',
            'flight'
        )
        model = Passengers
        depth = 2

class Flights(serializers.ModelSerializer):
    class Meta:
        fields = (
            'origin',
            'destination',
            'duration'
        )
        model = journey
        depth = 2
