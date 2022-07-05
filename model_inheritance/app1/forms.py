from django import forms
from .models import User,User2

class StudentForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['student_name','email','password']

		widgets={'password':forms.PasswordInput}


#Lets do inherit 

class TeacherForm(StudentForm):
	class Meta(StudentForm.Meta):
		fields=['teacher_name','email','password']


class ExtForm(forms.ModelForm):
	class Meta:
		model=User2
		fields=['student_name','teacher_name','email','password','address']


