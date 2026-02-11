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

    # Blog post CRUD URLs (ALX expects singular 'post' in paths)
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
