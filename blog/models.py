
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class quiz(models.Model):
	question = models.CharField(max_length=1000, default="")
	option1 = models.CharField(max_length=500, default="")
	option2 = models.CharField(max_length=500, default="")
	option3 = models.CharField(max_length=500, default="")
	option4 = models.CharField(max_length=500, default="")
	answer = models.CharField(max_length=500, default="")
	catogaries = models.CharField(max_length=500,default="")
	hint = models.CharField(max_length=500, default="")
	like=models.IntegerField(default=0)
	dislike=models.IntegerField(default=0)
	student = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.catogaries)


class Attempts(models.Model):
	attemptId = models.AutoField(primary_key=True)
	q_name = models.CharField(max_length=500, default="",null=True)
	qAttempter = models.CharField(max_length=500, default="",null=True)
	totalQue = models.IntegerField(default= 0 )
	attemptedQue = models.IntegerField(default= 0)
	correct = models.IntegerField(default= 0)
	accuracy = models.IntegerField(default= 0)
	attemptedtime = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return str(self.attemptId)


class Test(quiz):
	testId = models.CharField(max_length=500)
	Quiz_cover = models.ImageField(upload_to ='QuizCover',null=True,blank=True) 
	def __str__(self):
		return str(self.catogaries)