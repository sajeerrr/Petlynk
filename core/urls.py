from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='user_login'),
    path('register/', views.register, name='register'),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
