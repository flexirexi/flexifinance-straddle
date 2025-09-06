from django.shortcuts import render


def index(request):
    return render(request, 'account/login.html')


def dashboard(request):
    return render(request, 'main/dashboard.html')


def calculate(request):
    return render(request, 'main/calculate.html')


def analysis(request):
    return render(request, 'main/analysis.html')

