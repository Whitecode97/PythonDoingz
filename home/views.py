from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "home/index.html")

def earn(request):
    return render(request, "home/earn.html")

def lotto(request):
    return render(request, "home/lotto.html")

# the html access links for all views
# http://127.0.0.1:8000/home/
# http://127.0.0.1:8000/home/earn/
# http://127.0.0.1:8000/earn/lotto/
# https://github.com/Whitecode97/PythonDoingz.git