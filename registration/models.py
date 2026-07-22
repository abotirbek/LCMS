from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, LoginForm, ProfileForm, ResetPasswordForm, ChangePasswordForm
from .models import Profile, CustomUser, Code
from config.settings import EMAIL_HOST_USER
from .utils import send_login_email
from datetime import datetime

# Create your views here.

def register_view(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            send_mail(
                subject='Welcome to E-Product',
                message='Enjoy buying many products in low prices and various categories!\nEnter this 6-digit code ',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False
            )
            Profile.objects.create(user = user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('product_list')
            else:
                return redirect('register')
    else:
        form=RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('product_list')
            else:
                return redirect('register')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

def get_profile(request):
    user = request.user
    if user:
        profile = Profile.objects.get(user=user)
    else:
        return redirect('product_list')
    return render(request, 'accounts/profile.html', {'profile': profile})

def edit_profile(request):
    profile = None
    user = request.user
    if user:
        profile = Profile.objects.get(user = user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance = profile)
    return render(request, 'accounts/edit_profile.html', {'form':form})

def send_email_code(request):
    if request.method=='POST':
        form=ResetPasswordForm(request.POST)
        if form.is_valid():
            user=CustomUser.objects.get(username=form.cleaned_data.get('username'),email=form.cleaned_data.get('email'))
            if user:
                code = Code.objects.create(user=user)
                send_login_email(user, code.code)
                return redirect('send')
    else:
        form=ResetPasswordForm()
    return render(request,"accounts/reset_password.html", {'form': form})

def change_password(request):
    username = request.GET.get("name", "").rstrip("/")
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('new_password')
            code=form.cleaned_data.get('code')
            user=CustomUser.objects.get(username=username)
            if user:
                code_user=Code.objects.filter(user=user,code=code,expire_date__gt=datetime.now()).first()   # 18:22 18:21
                if code_user:
                    user.set_password(password)
                    user.save()
                    login(request, user)
                    return redirect('product_list')
                else:
                    return redirect('login')
    else:

        form=ChangePasswordForm()
    return render(request,'accounts/change_password.html',{'form':form })
