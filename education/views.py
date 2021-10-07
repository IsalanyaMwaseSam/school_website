from django.shortcuts import render
from django.contrib.auth import authenticate, login


app_name = 'education'
# Create your views here.
def home(request):
    return render(request, 'education/home.html', {})

def computing(request):
    return render(request, 'education/computing.html', {})

def business(request):
    return render(request, 'education/business.html', {})

def education(request):
    return render(request, 'education/education.html', {})

def graduation(request):
    return render(request, 'education/graduation.html', {})

def growth(request):
    return render(request, 'education/growth.html', {})

def health(request):
    return render(request, 'education/health.html', {})

def computing(request):
    return render(request, 'education/computing.html', {})

def research(request):
    return render(request, 'education/research.html', {})

def social(request):
    return render(request, 'education/social.html', {})

def theology(request):
    return render(request, 'education/theology.html', {})

def about(request):
    return render(request, 'education/about.html')

def application(request):
    return render(request, 'education/application.html')


def starter(request):
    return render(request, 'education/starter.html')

def elearning(request):
    return render(request, 'education/e-learning.html')







