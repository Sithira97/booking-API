from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets
from .serializers import MenuSerializer, UserSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create your views here.
class MenuView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]