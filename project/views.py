from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, ProfileForm, CourseRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
        authors = Authors.objects.select_related('course').all()
       
        return render(request, 'index.html', {"authors":authors}) 

@login_required(login_url='/account/loginpage')
def dashboard(request):
        username = request.session['username']
        user = User.objects.get(username = username)
        profile = Profile.objects.filter(user_id=user.id).all()
        Reg = Registration.objects.select_related('creg').filter(user_id=user.id)
        context = {'profile':profile, 'Reg':Reg}
        
        return render(request, 'account/dashboard.html', context)

def register(request):
        form = CreateUserForm()
        if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                        form.save()
                        user = form.cleaned_data.get('username')
                        messages.success(request, "Account successfully created for" + user)
                        return redirect('profile')
                        
        context = {"form":form}                
        return render(request, 'account/register.html',context)


def loginpage(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                
                request.session['username']=username
                
                user = authenticate(request, username=username, password=password)
                if user is not None and user.get_username()!="chrissy":
                        login(request, user)
                        return redirect('account/dashboard')
                
                elif  user.get_username()=="chrissy":
                        login(request, user)
                        return redirect('user_dashboard')               
                else:
                        messages.info(request, "Username or password not found!")

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
                        return redirect('account/user_dashboard')
        context ={'form':form}
        return render(request, "account/profile.html", context)

def deleteProfile(request, pk):
        profile = Profile.objects.get(id=pk)
        if request.method == 'POST':
                profile.delete()
                return redirect('user_dashboard')
        context = {'item':profile}
        return render(request, 'account/delete.html', context)

def course_registration(request):
        form = CourseRegistrationForm()
        if request.method == 'POST':
                form = CourseRegistrationForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('account/dashboard/')
        context = {'form':form}
        return render(request, "account/course_registration.html", context)

def update_course_registration(request):
        return redirect(request, 'account/course_registration.html')

@login_required(login_url='/account/loginpage')
def course_detail(request, pk):
        profile = Authors.objects.select_related('course').filter(id=pk)
        context = {'profile':profile}
        return render(request, "account/course_detail.html", context)

def user_dashboard(request):
        count_smm =  Registration.objects.filter(creg_id=7).count()
        count_gwd =  Registration.objects.filter(creg_id=8).count()
        count_mc =  Registration.objects.filter(creg_id=9).count()
        count_bm =  Registration.objects.filter(creg_id=11).count()
        profile = Profile.objects.select_related('user').all()
        context = {'profile':profile, 'count_smm,':count_smm, 'count_gwd':count_gwd, 'count_mc':count_mc, 'count_bm':count_bm}
        return render(request, 'account/user_dashboard.html', context)

