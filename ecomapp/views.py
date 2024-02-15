from django.shortcuts import render,redirect
from item.models import *
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import logout as lg

# Create your views here.
def index(request):
    items = Items.objects.filter(is_sold = False)[:6]
    categories = Category.objects.all()
    return render(request, 'ecomapp/index.html', {
        'categories':categories,
        'items': items,
    })

def contact(request):
    return render(request, 'ecomapp/contact.html')

def about(request):
    return render(request, 'ecomapp/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'ecomapp/signup.html', {
        'form': form
    })

def logout(request):
    lg(request)
    return redirect('/login/')