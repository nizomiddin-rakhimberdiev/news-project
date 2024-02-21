from django.shortcuts import render, redirect
from . models import Task,UserProfile

from . forms import RegisterUserFrom,LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def main_page(request):
    tasks = Task.objects.all()

    return render(request, 'index.html', context={'tasks': tasks})

def about_page(request):
    return render(request, 'about.html', context={})


def register_view(request):
    if request.method == 'POST':
        form = RegisterUserFrom(request.POST)

        if form.is_valid():
            user = form.save()

            UserProfile.objects.Create(user)

            return redirect('login')

    else:
        form = RegisterUserFrom()

    return render(request, 'registration/register.html', context={"form": form })


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username = username, password = password)

            if user:
                login(request, user)

                return redirect('/')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', context={"form": form })