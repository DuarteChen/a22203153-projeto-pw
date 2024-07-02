from django.shortcuts import render
from .models import *
from datetime import datetime
from django.shortcuts import render, redirect
from .utils import divide_subjects_byYear
from django.contrib.auth import models,login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *

def contextFun(request):
    username = request.user.username if request.user.is_authenticated else 'Guest'

    context = {
        'anoAtual' : datetime.today().year,
        'username': username
    }

    return context


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect('portfolio:portfolio')  # Redirect to a homepage or dashboard
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    context = contextFun(request)
    context['form'] = 'form'

    return render(request, 'auth/login.html', context)


def user_view(request):
    context = contextFun(request)
    return render(request, 'auth/user.html', context)



def logout_view(request):
    logout(request)
    return redirect('portfolio:portfolio')


def registo_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password']
            )
            messages.success(request, "User registered successfully.")
            return redirect('portfolio:login')
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        form = UserRegistrationForm()

    context = contextFun(request)
    context['form'] = form

    return render(request, 'auth/registo.html', context)



def aboutMe_view(request):

    context = contextFun(request)

    return render(request, "portfolio/aboutme.html", context)

def portfolio_view(request):
    username = request.user.username if request.user.is_authenticated else 'Guest'
    curso = Course.objects.get(name="Engenharia Informática")

    context = contextFun(request)
    context['subjects'] = Subject.objects.all()
    context['curso'] = curso

    return render(request, "portfolio/portfolio.html", context)

def subject_view(request, subjectId):
    username = request.user.username if request.user.is_authenticated else 'Guest'

    context = contextFun(request)
    contect['subject'] = Subject.objects.get(id=subjectId)

    return render(request, "portfolio/subject.html", context)


