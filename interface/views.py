from django.shortcuts import render
import static.pages.regiones
# Create your views here.
def index(request):

    return render(request, 'home.html', {})

def regionUno(request):

    return render(request, 'pages/region-uno.html', {})