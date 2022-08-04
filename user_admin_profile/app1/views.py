from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import UForm,User_Change,Admin_Change
from django.contrib.auth.models import User
# Create your views here.

def SignUp(request):
    if request.method=='POST':
        form=UForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Signup successfully')
    else:
        form=UForm()
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
        return HttpResponseRedirect('/login/')
    return render(request,'app1/login.html',{'form2':form2})

def profile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            if request.user.is_superuser==True:
                users=User.objects.all()
                form=Admin_Change(request.POST,instance=request.user)
            else:
                users=None
                form=User_Change(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,'Saved successfully')
       
        else:
            if request.user.is_superuser==True:
                users=User.objects.all()
                form=Admin_Change(instance=request.user)
            else:
                users=None
                form=User_Change(instance=request.user)
            
        return render(request,'app1/profile.html',{'name':request.user,'form':form,'users':users})#we can add request.user.email,request.user.username
       
    else:
        return HttpResponseRedirect('/login/')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def change_password(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'password change successfully')
                update_session_auth_hash(request,form.user)
                return HttpResponseRedirect('/profile/')#this is will not redirect becuase session will be wiped out so need to keep updated
        else:
            form=PasswordChangeForm(user=request.user)
    
        return render(request,'app1/changepassword.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def UserDetail(request,uid):
    if request.user.is_authenticated:
        data=User.objects.get(pk=uid)
        form=Admin_Change(instance=data)#for viewing detail we will use form
        return render(request,'app1/userdetail.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

