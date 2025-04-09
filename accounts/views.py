from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:home')
    else:
        form = StudentRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def login_success_view(request):
    return render(request, 'registration/login_success.html')

def home(request):
    return render(request, 'home.html')

@login_required
def daily_tasks(request):
    return render(request, 'accounts/daily_tasks.html')

@login_required
def create_plan(request):
    return render(request, 'accounts/create_plan.html')


@login_required
def deadline_tracker(request):
    return render(request, 'accounts/deadline_tracker.html')

def home(request):
    return render(request, 'accounts/home.html')  # Simple home page view

@login_required
def track_progress_static(request):
    return render(request, 'accounts/track_progress.html')