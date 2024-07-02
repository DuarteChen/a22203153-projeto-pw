from django.shortcuts import render
from .models import *
from datetime import datetime
from django.shortcuts import render, redirect
from .utils import divide_subjects_byYear
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def ano():
    anoAtual = datetime.today().year

    return anoAtual

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

    context = {
        'anoAtual' : ano(),
        'form': form
    }
    return render(request, 'auth/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('portfolio:portfolio')

def aboutMe_view(request):

    context = {

        'anoAtual' : ano(),
    }

    return render(request, "portfolio/aboutme.html", context)

def portfolio_view(request):
    curso = Course.objects.get(name="Engenharia Informática")

    context = {
        'anoAtual' : ano(),
        'curso': curso,
        'subjects' : Subject.objects.all()
    }

    return render(request, "portfolio/portfolio.html", context)

def subject_view(request, subjectId):

    context = {
        'anoAtual' : ano(),
        'subject' : Subject.objects.get(id=subjectId)
    }

    return render(request, "portfolio/subject.html", context)
