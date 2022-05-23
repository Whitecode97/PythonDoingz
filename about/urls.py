from django.urls import path

from home.views import home
from .views import about
from earn.views import earn

urlpatterns = [
    path("", home),
    path("about/", about),
]