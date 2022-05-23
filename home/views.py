from django.shortcuts import render

from earn.views import withdraw

# Create your views here.


def home(request):
    return render(request, "home/index.html")

# the html access links for all apps
# http://127.0.0.1:8000/home/
# http://127.0.0.1:8000/home/about/
# http://127.0.0.1:8000/home/earn/
# http://127.0.0.1:8000/earn/lotto/
# http://127.0.0.1:8000/earn/withdraw/