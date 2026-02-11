from django.urls import path
from django.shortcuts import render

def home(request):
    return render(request, 'blog/base.html')

urlpatterns = [
    path('', home, name='home'),
]
