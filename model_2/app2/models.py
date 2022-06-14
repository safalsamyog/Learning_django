from django.db import models

# Create your models here.
class Biodata(models.Model):
    Id=models.IntegerField(max_length=10,primary_key=True)
    name=models.CharField(max_length=15)
    address=models.CharField(max_length=12)
    mail=models.CharField(max_length=25)

    # def __str__(self):
    #     return self.name