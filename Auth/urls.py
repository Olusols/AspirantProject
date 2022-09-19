from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    #path('login/', views.LoginView.as_view(template_name='auth/login.html'), name ='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    path("register/", views.register, name="register"),
    path('welcome/', views.welcome, name='welcome'),
    path('user-detail/', views.user_detail, name='user-detail'),
]