from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.views import redirect_to_login, logout_then_login
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
        return redirect_to_login(resolve_url('/restaurant/book'))

    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    context = {'form': form, 'user': request.user}
    return render(request, 'book.html', context)


def logout_view(request):
    return logout_then_login(request)
