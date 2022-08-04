from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User,Group
# Create your views here.

def SignUp(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            fm=form.save()
            group=Group.objects.get(name='Editor')
            fm.groups.add(group)
            messages.success(request,'Signup successfully')
    else:
        form=UserCreationForm()
    return render(request,'app1/signup.html',{'form':form})

def log_in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form2=AuthenticationForm(request=request,data=request.POST)#in this form we need to give two parameters
            if form2.is_valid():
                username=form2.cleaned_data['username']
                password=form2.cleaned_data['password']
            
                user=authenticate(username=username,password=password)
            
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/dashboard/')

            
            
        else:
            form2=AuthenticationForm()
    else:
        return HttpResponseRedirect('/login/')
    return render(request,'app1/login.html',{'form2':form2})

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'app1/dashboard.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')