from django.urls import path
from django.shortcuts import render
from . import views

def home(request):
    return render(request, 'blog/base.html')

urlpatterns = [
    path('', home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
