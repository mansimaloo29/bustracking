from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Route,Driverdetails,Image


    
    
    


class CreateUserForm(UserCreationForm):
    
    TYPE=(('0','Student'),('1','Driver'),)
    role = forms.ChoiceField( choices=TYPE)
    # gender = forms.ChoiceField(widget=forms.RadioSelect(
    # 	choices=User.GENDER_CHOICES), help_text="Gender")
    class Meta:
    	model = User
    	fields=['username','email','password1','password2','role']
        
    	  
		
		


class Routeform(ModelForm):
	class Meta:
		model= Route
		fields=['source','destination','routeno']


class Driverdetailsform(ModelForm):
	class Meta:
		model= Driverdetails
		fields='__all__'

	
	


class PasswordChangingForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={'style':' display: block;margin-top:1%;width:300px;border:none;padding:10px 15px;border-radius:20px;background:#F1F4F8;','class':'form-control','type':'password'}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'style':' display: block;margin-top:1%; display: block;width:300px;border:none;padding:10px 15px;border-radius:20px;background:#F1F4F8;','class':'form-control','type':'password'}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'style':' display: block;margin-top:1%;width:300px;border:none;padding:10px 15px;border-radius:20px;background:#F1F4F8;','class':'form-control','type':'password'}))
	
	class Meta:
		model = User
		fields=('old_password','new_password1','new_password2')


# class Showroutesform(ModelForm):
# 	class Meta:
# 		model= Showroutes
# 		fields='__all__'		

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=("caption","image")