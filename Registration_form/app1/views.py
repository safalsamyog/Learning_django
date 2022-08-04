
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #we are using already made forms from this applications 
from .forms import SignUpForm
from django.contrib import messages
# Create your views here.
def Sign_Up(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #it will save in its own databse
    else:
        form=UserCreationForm()
    return render(request,'app1/index.html',{'form':form})


def Sign_Up_more(request):
    
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save() #it will save in its own databse
            messages.success(request,'From saves successssfully')
    else:
        form=SignUpForm()
    return render(request,'app1/index2.html',{'form2':form})

