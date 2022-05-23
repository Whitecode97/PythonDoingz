from django.shortcuts import render

# Create your views here.


def earn(request):
    return render(request, "earn/earn.html")

def lotto(request):
    return render(request, "earn/lotto.html")

def withdraw(request):
    return render(request, "earn/withdraw.html")



