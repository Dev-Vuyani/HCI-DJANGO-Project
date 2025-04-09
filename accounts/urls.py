from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('login/success/', views.login_success_view, name='login_success'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Removed task_manager completely
    path('daily-tasks/', views.daily_tasks, name='daily_tasks'),
    path('create-plan/', views.create_plan, name='create_plan'),
    path('deadlines/', views.deadline_tracker, name='deadline_tracker'),
    path('track-progress/', views.track_progress_static, name='track_progress'),
    
]