from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest,HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'name': 'Ruslan',
        'age': 49,
        'email': 'bigun.ruslan@gmail.com'
    }
    return render(request, 'base.html', context)
