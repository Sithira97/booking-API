from django.shortcuts import render, redirect, resolve_url, get_list_or_404
from django.contrib.auth.views import redirect_to_login, logout_then_login
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import MenuSerializer, UserSerializer, BookingSerializer
from .models import Menu, Booking
from .forms import BookingForm

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def menu(request):
    return render(request, 'menu.html', {})


def book(request):
    if not request.user.is_authenticated:
        return redirect_to_login(resolve_url('/book'))

    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    context = {'form': form, 'user': request.user}
    return render(request, 'book.html', context)


def bookings(request):
    if not request.user.is_authenticated:
        return redirect_to_login(resolve_url('/bookings'))
    query = Booking.objects.all().filter(name=request.user.username)
    serializer = BookingSerializer(query, many=True)
    return render(request, 'bookings.html', {'bookings' :serializer.data})

def logout_view(request):
    return logout_then_login(request)


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MenuView(generics.ListCreateAPIView):
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
    pagination_class = None

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Booking.objects.all()
        elif self.request.user.groups.count() == 0:
            return Booking.objects.all().filter(name=self.request.user.username)
