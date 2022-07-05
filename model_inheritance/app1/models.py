from django.db import models

# Create your models here.
class User(models.Model):
	student_name=models.CharField(max_length=50)
	teacher_name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	password=models.CharField(max_length=50)


class User2(User):#here i did inheritance here
	address=models.CharField(max_length=50)