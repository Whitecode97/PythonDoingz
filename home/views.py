from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")

# the html access links for all views
# http://127.0.0.1:8000/home/
# http://127.0.0.1:8000/home/about/
# http://127.0.0.1:8000/home/contact/
# https://github.com/Whitecode97/PythonDoingz.git