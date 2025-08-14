from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserSignupForm

def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = UserSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect_user_dashboard(request.user)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect_user_dashboard(user)
        messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def redirect_user_dashboard(user):
    if getattr(user, 'user_type', 'patient') == 'doctor':
        return redirect('accounts:doctor-dashboard')
    return redirect('accounts:patient-dashboard')

@login_required
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html')
