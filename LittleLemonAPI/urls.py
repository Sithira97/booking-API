from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('menu-items/', views.MenuView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
]
