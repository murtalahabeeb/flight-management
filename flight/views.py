from django.shortcuts import render
from rest_framework import generics

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    return render(request, "flights/index2.html", {
        "flights": journey.objects.all()
    })


def travel(request, flight_id):
    f = journey.objects.get(pk=flight_id)
    nonPassanger = Passengers.objects.exclude(flight=f).all()
    return render(request, "flights/flight.html", {
        "flight": f,
        "nonPassangers": nonPassanger

    })


def book(request, flight_id):
    if request.method == "POST":
        getflight = journey.objects.get(pk=flight_id)
        person = Passengers.objects.get(pk=int(request.POST["Passanger"]))
        person.flight.add(getflight)
        return HttpResponseRedirect(reverse("flight:journey", args=(getflight.id,)))


