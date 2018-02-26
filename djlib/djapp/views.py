from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
# Create your views here.

def registration(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_name = data['username']
            email = data['email']
            password = data['password']
            if not User.objects.filter(username=user_name).exists() and \
                not User.objects.filter(email=email).exists():
                User.objects.create_user(user_name, email, password)
                user = authenticate(username=user_name, password=password)
                login(request, user)
                return HttpResponseRedirect('/')

        else:
            return form.ValidationError("Invalid form")

    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')

