from django.contrib import admin
from .models import User,User2
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display=('student_name','teacher_name','email','password')


@admin.register(User2)
class User2Admin(UserAdmin):#here i did inheritance too
	pass

