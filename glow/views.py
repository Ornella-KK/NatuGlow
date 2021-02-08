from django.shortcuts import render,redirect
from django.http import Http404
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    routine = Routine.objects.all()
    
    context = {
        'routine':routine,
    }
    return render(request,'index.html',context)
