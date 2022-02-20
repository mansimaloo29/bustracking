from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


# class Registration(models.Model):
# 	TYPE=(('0','Student'),('1','Driver'),)
# 	username=models.CharField(max_length=15)
# 	email=models.CharField(max_length=30)
# 	password=models.CharField(max_length=15)
# 	role = models.CharField(max_length=200, null=True, choices=TYPE)






class Registration(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default = 1)
	TYPE=(('1','Student'),('2','Driver'),)
	role = models.CharField(max_length=200, null=True, choices=TYPE)
	mobile=models.CharField(max_length=20,default ="")
	def __str__(self):
		return f"{self.user.first_name}  {self.user.last_name}"

class Route(models.Model):
    source = models.CharField(max_length=12)
    destination = models.CharField(max_length=12)
    routeno=models.IntegerField(null=True)



    def __str__(self):
        return f"{self.source} to {self.destination}"

class Driverdetails(models.Model):
	busNo = models.IntegerField(blank=True, null=True)
	driverName = models.CharField(max_length=12)
	selectroute = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="buses")
	def __str__(self):
		return f"{self.driverName}-{self.busNo} - {self.selectroute} "





        




# class Showroutes(models.Model):
# 	selectroutes=models.ForeignKey(Route,null=True,on_delete=models.SET_NULL)

# class Showbus(models.Model):
# 	showbus = models.ForeignKey(Driverdetails, null=True, on_delete= models.SET_NULL)

class complaint(models.Model):
    name=models.CharField(max_length=20)
    busno=models.CharField(max_length=20)
    complaints=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} {self.busno}"

class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    date = models.DateField(default=datetime.now)
    def __str__(self):
    	return self.caption

class businformation(models.Model):
    busnumber=models.CharField(max_length=20)
    busplateno=models.CharField(max_length=20)
    def __str__(self):
        return self.busnumber







