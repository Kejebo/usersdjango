from django.urls import path
from . import views

app_name='app_users'

urlpatterns = [
    path(
        'register/',
        views.RegisterUser.as_view(),
        name='user_register'
    ),
    path(
        'login/',
        views.Login.as_view(),
        name='login'
    ),
    path(
        'logout',
        views.Logout.as_view(),
        name='logout'),
    path(
        '',
        views.Home.as_view(),
        name='home'),
    path(
        'changes_password',
        views.UpdatePassword.as_view(),
        name='changes_password')
    
    
]
