from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='loginBrowser'),
    path('logout/', views.logout_view, name='logoutBrowser'),
]
