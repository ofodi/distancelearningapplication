from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, ProfileForm, CourseRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
        authors = Authors.objects.select_related('course').all()
       
        return render(request, 'index.html', {"authors":authors}) 

def dashboard(request):
        return render(request, 'account/dashboard.html')

def register(request):
        form = CreateUserForm()
        if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                        form.save()
                        user = form.cleaned_data.get('username')
                        messages.success(request, "Account successfully created for" + user)
                        return redirect('account/dashboard')
                        
        context = {"form":form}                
        return render(request, 'account/register.html',context)


def loginpage(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                
                request.session['username']=username
                
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        return redirect('account/dashboard')
        return render(request, 'account/loginpage.html')

def logoutUser(request):
        logout(request)
        return redirect('index')

def createprofile(request):
        form = ProfileForm()
        if request.method == 'POST':
                form = ProfileForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect("account/dashboard")
        context ={'form':form}
        return render(request, "account/profile.html", context)

def editprofile(request, pk):
        profile = Profile.objects.get(id=pk)
        form = ProfileForm(instance=profile)
        if request.method == 'POST':
                form = ProfileForm(request.POST, instance=profile)
                if form.is_valid():
                        form.save()
                        return redirect('account/dashboard')
        context ={'form':form}
        return render(request, "account/profile.html", context)

def course_registration(request):
        form = CourseRegistrationForm()
        if request.method == 'POST':
                form = CourseRegistrationForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('account/dashboard')
        context = {'form':form}
        return render(request, "account/course_registration.html", context)

def update_course_registration(request):
        return redirect(request, 'account/course_registration.html')

@login_required(login_url='/account/loginpage')
def course_detail(request, pk):
        profile = Authors.objects.select_related('course').filter(id=pk)
        context = {'profile':profile}
        return render(request, "account/course_detail.html", context)

