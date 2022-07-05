from django.shortcuts import render
from .models import User
from .forms import UserForm
from django.contrib import messages
from django.contrib.messages import get_messages
# Create your views here.

def Fun1(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()#saving without cleaned_data
			messages.add_message(request,messages.SUCCESS,'Saved sucessfully')

			messages.debug(request,'This is debug')#this will not shown in templates becuase this is not set
			print(messages.get_level(request))
			messages.set_level(request,messages.DEBUG)#this should be always in the up
			messages.debug(request,'This is new debug')

			#shortcut 
			messages.info(request,'Now ur add is added')
			messages.error(request,'error')
			messages.warning(request,'warning')

			#This will only work inside the messages box
			messages_1=get_messages(request)

			for msg in messages_1:
				print(msg)
	else:
		form=UserForm()
	
	return render(request,'app1/index.html',{'form':form})


'''
So in messsages framework debug will not show becuase its value is 10 so above 10 all value is seen
So for showing debug we used get_level and set_level

'''