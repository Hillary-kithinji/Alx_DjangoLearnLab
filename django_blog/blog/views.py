from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# Registration view
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Login failed. Check username and password.")
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

# Profile view
@login_required
def profile_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        request.user.email = email
        request.user.save()
        messages.success(request, "Profile updated successfully!")
    return render(request, 'blog/profile.html', {'user': request.user})
