from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signin(request):
    return render(request, 'signin.html')
def homepage(request):
    return render(request, 'homepage.html')
def signup(request):
    return render(request, 'signup.html')
def setting(request):
    return render(request, 'setting.html')