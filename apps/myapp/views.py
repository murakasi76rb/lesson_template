from django.shortcuts import render
from apps.myapp.models import MenuItem
# Create your views here.
from django.http import HttpRequest,HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'name': 'Ruslan',
        'age': 49,
        'email': 'bigun.ruslan@gmail.com'
    }
    return render(request, 'myapp/index.html', context)



def menu(request:HttpRequest) -> HttpResponse:
    menu = MenuItem.objects.all()
    context = {
        'menu': menu,
    }
    return render(request, 'myapp/menu.html', context)
