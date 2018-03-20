from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from .models import DjUser, Book
import datetime
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
# Create your views here.

def registration(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_name = data['username']
            email = data['email']
            password = data['password']
            if not DjUser.objects.filter(username=user_name).exists() and \
                not DjUser.objects.filter(email=email).exists():
                DjUser.objects.create_user(user_name, email, password)
                user = authenticate(username=user_name, password=password)
                login(request, user)
                form.save()
                return HttpResponseRedirect('/')

        else:
            return form.ValidationError("Invalid form")

    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')

def list_book(request):
   
    d = DjUser.objects.get(username=request.user.username)
    #a = Book.objects.get_or_create(book_user=d,name='MachineLearning', edition='5', author='abc', publisher='xyz', issue_date=datetime.datetime.now())
    #a = Book(book_user=d,name='MachineLearning', edition='5', author='abc', publisher='xyz', issue_date=datetime.datetime.now())
    #a.save()
    data = Book.objects.filter(book_user=d).distinct()

    return render(request, 'book_list.html', {'book_data': data})


class BookView(ListView):

    model = Book
    template_name = 'book_list.html'
    context_object_name = 'book_data'

    def get_queryset(self):
        d = DjUser.objects.get(username=self.request.user.username)
        data = Book.objects.filter(book_user=d).distinct()
        return data



