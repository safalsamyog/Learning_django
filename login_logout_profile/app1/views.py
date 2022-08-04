from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def SignUp(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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
                    return HttpResponseRedirect('/profile/')

            
            
        else:
            form2=AuthenticationForm()
    else:
        return HttpResponseRedirect('/profile/')
    return render(request,'app1/login.html',{'form2':form2})

def profile(request):
    if request.user.is_authenticated:
        return render(request,'app1/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')