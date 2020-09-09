from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from flight.models import *


# Create your views here.

class ListPassengers(generics.ListCreateAPIView):
    queryset = Passengers.objects.all()
    serializer_class = Passenger


class DetailedPassengers(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passengers.objects.all()
    serializer_class = Passenger


class ListFlights(generics.ListCreateAPIView):
    queryset = journey.objects.all()
    serializer_class = Flights


class DetailedFlights(generics.RetrieveUpdateDestroyAPIView):
    queryset = journey.objects.all()
    serializer_class = Flights
