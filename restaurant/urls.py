from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('bookings/', views.bookings, name='bookings'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='loginBrowser'),
    path('logout/', views.logout_view, name='logoutBrowser'),
    path('api/menu-items/', views.MenuView.as_view(), name="menuItems"),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/booking/', include(router.urls)),
]
