from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def home_screen_view(request):
    return render(request, 'base.html', {})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})

def home_view(request):

    return render(request, 'account/home.html', {})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data =  request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {"form": form})

def logout_view(request):
    logout(request)
    return render(request, 'account/logout.html', {})

