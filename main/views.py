from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def account(request):
    return render(request, 'account.html')

def home(request):
    return render(request, 'home.html')

def newpost(request):
    return render(request, 'newpost.html')

def newsfeed(request):
    return render(request, 'newsfeed.html')

def postdetails(request):
    return render(request, 'postdetails.html')

def profile(request):
    return render(request, 'profile.html')

def search(request):
    return render(request, 'search.html')

def settings(request):
    return render(request, 'settings.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')
