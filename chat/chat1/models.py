from django.db import models

# Create your models here.
class Loggers(models.Model):
	name= models.CharField(max_length=120)
	title= models.CharField(max_length=300, unique=True)
	text1=models.IntegerField()
	text2=models.IntegerField()
	text3=models.IntegerField()
	text4=models.IntegerField()
	text5=models.IntegerField()
	text6=models.IntegerField()
	text7=models.IntegerField()
	text8=models.IntegerField()
	text9=models.IntegerField()
