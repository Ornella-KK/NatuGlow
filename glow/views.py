from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def home(request):
    routine = Routine.objects.all()
    skin = Category.objects.all()
    comment = Comment.objects.all()
    title = 'Home'
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = int(request.POST.get("idpost"))
            post = Post.objects.get(id = post_id)
            comment = form.save(commit=False)
            comment.username = request.user
            comment.post = post
            comment.save()
        return redirect('index')

    else:
        form = CommentForm()

    return render(request,'index.html', {'routine':routine,'skin':skin,'comment':comment, 'form':form,'title':title})

def page_category(request,category):
    skin = Category.objects.all()
    title = f"{category}"
    category_results = Image.search_by_category(category)
    return render(request,'index.html',{'routine':category_results,'skin':skin,'title':title})

def search_results(request):
    if 'names' in request.GET and request.GET['names']:
        search_term = request.GET.get("names")
        searched_routines = Routine.search_by_routine(search_term)
        
        message = f'{search_term}'
        
        return render(request,'search.html',{"message":message,"routines":searched_routines})
    
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message,"routines":searched_routines})

def post_routine(request):
    current_user = request.user
    if request.method == 'POST':
        form = RoutineForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.profile =current_user
            form.save()
        return redirect('home')
    else:
        form =RoutineForm()
            
    return render(request,'uploads.html',{"form":form,})

