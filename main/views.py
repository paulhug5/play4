from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm

# Create your views here.

#home
def home(request):
    return render(request, 'main/home.html')

#registration form validation
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = RegistrationForm()

    return render(request, 'main/register.html', {'form': form})

#login form
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # Get the username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:home')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'main/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('main:home')