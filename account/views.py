from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home_screen_view(request):
    return render(request, 'base.html', {})

def register_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('user_account')
    else:
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
    user = request.user
    if user.is_authenticated:
        return redirect('user_account')
    else:
        if request.method == "POST":
            form = AuthenticationForm(data =  request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('user_account')
        else:
            form = AuthenticationForm()
    return render(request, 'account/login.html', {"form": form})

def logout_view(request):
    logout(request)
    return redirect('home')

