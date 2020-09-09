from django.urls import path
from . import views

app_name = "flight"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.travel, name="journey"),
    path("<int:flight_id>/book", views.book, name="book"),
]
