from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
# Create your views here.

def sing_in(request):
    error = False
    message = ''
    if request.method == "POST":
        cuid = request.POST.get('cuid', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(username=cuid).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('home-index')
            else:
                error = True
                message = 'Your password is incorrect'
                print("mot de pass incorrecte")
        else:
            error = True
            message = "you don't have the permission to use this application"
            print("User does not exist")
    context = {
        'error':error,
        'message':message
    }

    return render(request, 'register.html', context)

@login_required(login_url='sing_in')

def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')


    