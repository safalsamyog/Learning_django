from django.db import models

# Create your models here.

class Std_data(models.Model):
    std_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=90)
    email=models.EmailField(max_length=90)
    #Lets update another here
    address=models.CharField(max_length=16,default="Nothing here")
    #after doing some updates we must give a deafult value 
    def __str__(self):
        return self.name
        #return str(self.std_id)
        #condtion for int field


#lets do migrations and do migrates

#def __str__(self):
#   return self.field_name

#this is used for showing proper objects name to see

#we can add any data

