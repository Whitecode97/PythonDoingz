from django.urls import path

from home.views import home
from about.views import about
from .views import  earn,lotto,withdraw


urlpatterns = [
    path("earn/", earn),
    path("lotto/", lotto),
    path("withdraw/", withdraw),
]