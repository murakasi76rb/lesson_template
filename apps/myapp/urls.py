from django.urls import path
from apps.myapp import views

app_name = 'myapp'

urlpatterns = [
path('index/', views.index, name='index'),
path('menu/', views.menu, name='menu'),
]
