from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import BookingForm, LoginForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def menu(request):
    return render(request, 'menu.html', {})

def book(request):
    if  not request.user == 'AnonymousUser':
        return redirect('loginBrowser')

    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    context = {'form':form, 'user':request.user}
    return render(request, 'book.html', context)


def loginBrowser(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url, permanent=True)
                else:
                    return redirect('home', permanent=True)
    context = {'form':form}
    return render(request, 'login.html', context)
