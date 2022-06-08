from unittest import load_tests
from django.urls import path

from .views import home, about,contact

app_name = "home"

urlpatterns = [
    path("", home, name="index.html"),
    path("about/", about, name="about.html"),
    path("contact/", contact, name="contact.html") 
]
