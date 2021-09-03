from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login as dj_login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(login_url='login')
def home(request):
     return render(request,'index.html')


#=============LOGIN==============#

def login(request):
    return render(request,'login.html')
