from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'index.html', {})


def regionUno(request):

    return render(request, 'pages/regiones/region-uno.html', {'don': 45})


def tableTemperatura(request):

    return render(request, 'pages/tables/temperature-table.html', {})

def tableHumedad(request):

    return render(request, 'pages/tables/temperature-table.html', {})

def tableSonido(request):

    return render(request, 'pages/tables/temperature-table.html', {})

def tableCO2(request):

    return render(request, 'pages/tables/temperature-table.html', {})

def chartTemperatura(request):

    return render(request, 'pages/charts/chart-temperatura.html', {})