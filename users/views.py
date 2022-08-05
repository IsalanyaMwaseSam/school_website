from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Courses, Profile, models




app_name = 'users'

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            messages.success(request, f'Your account has been created! You are now able to log in')
            current_user = request.user
            data = Profile()
            data.user_id = current_user.id
            data.save()
            messages.success(request, 'your account has been created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
       messages.MessageFailure(request, f'Invalid username or password, try again')


def course(request):
    course = Courses.objects.filter(user=request.user)
    context = {'courses':Courses}
    objects = models.Manager()
    for course in Courses:
        course = Courses.objects.get(id=user_obj.course_id)
    return render(request, 'education/starter.html', context)
   
             
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


def course(request):
    return render(request, 'users/course.html', {})

def staff(request):
    return render(request, 'users/staff.html', {})

