from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

from accounts.forms import SignInForm, SignupForm

# Create your views here.

# shurure UserCreationform use korbo


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {'form': SignupForm, 'error': 'Username has already taken'})
        else:
            return render(request, 'signup.html', {'form': SignupForm, 'error': 'Password Do not match'})
    else:
        return render(request, 'signup.html', {'form': SignupForm})


def loginView(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': SignInForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form': SignInForm,
                                                   'error': 'username and  password do no match'})
        else:
            login(request, user)
            return redirect('home')


def logoutAccount(request):
    logout(request)
    return redirect('home')
