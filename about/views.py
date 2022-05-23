from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def about(request):
    return render(request, "about/about.html")


