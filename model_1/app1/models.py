from django.db import models

# Create your models here.

class Data(models.Model):
	i_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=70)
	email=models.EmailField(max_length=70)
	#doing changes
	comment=models.CharField(max_length=40,default='nothing here')
	#we need to givve deafult value if we are adding
	




#for creating table through this class
# python manage.py makemigrations this dont make table but only migartions files
# python manage.py sqlmigrate app_name 0001 shows sql query
# python manage.py migrate for making the tables
