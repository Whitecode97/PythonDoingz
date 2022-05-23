from django.urls import path

from .views import home
from about.views import about
from earn.views import  earn

urlpatterns = [
    path("", home),
    path("about/", about),
    path("earn/", earn) 
]
