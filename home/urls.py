from unittest import load_tests
from django.urls import path

from .views import home, earn,lotto

urlpatterns = [
    path("", home),
    path("earn/", earn),
    path("lotto/", lotto) 
]
