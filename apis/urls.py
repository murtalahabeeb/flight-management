from django.urls import path
from . import views


urlpatterns = [
    path("",views.ListFlights.as_view()),
    path("<int:pk>",views.DetailedFlights.as_view()),
    path("passengers", views.ListPassengers.as_view()),
    path("<int:pk>", views.DetailedPassengers.as_view())
]
