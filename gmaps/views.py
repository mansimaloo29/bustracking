from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from .forms import Routeform,Driverdetailsform,PasswordChangingForm,ImageForm
import pyrebase
import twilio
from twilio.rest import Client
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
import string
import random
import http.client

# config = {
#    "apiKey": "AIzaSyDEuX4A78S5txhl1T-SsM7WBBMkFJIXmPk",
#     "authDomain": "maps-4d585.firebaseapp.com",
#     "databaseURL": "https://maps-4d585-default-rtdb.firebaseio.com",
#     "projectId": "maps-4d585",
#     "storageBucket": "maps-4d585.appspot.com",
#     "messagingSenderId": "98884066017",
#     "appId": "1:98884066017:web:72fd8695a934ad7a2bf5a0",
# }
config = {
    "apiKey": "AIzaSyDVif5V-QEaMfDuMa8TvVxWg6DTMpZDSyQ",
    "authDomain": "tracking-2fa5f.firebaseapp.com",
    "databaseURL":"https://tracking-2fa5f-default-rtdb.firebaseio.com",
    "projectId": "tracking-2fa5f",
    "storageBucket": "tracking-2fa5f.appspot.com",
    "messagingSenderId": "156615559135",
    
  };
firebase= pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()

def passwordgenerator():
    letters = string.ascii_letters
    finalpass =''.join(random.choice(letters) for i in range(4))

    # printing punctuation
    letters = string.punctuation
    finalpass += ''.join(random.choice(letters) for i in range(2))

    # printing digits
    letters = string.digits
    finalpass += ''.join(random.choice(letters) for i in range(3))    

    return finalpass

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    success_url=reverse_lazy('password_success')

def password_success(request):
    return render(request,'gmaps/password_success.html')

def home(request):
	return render(request, 'gmaps/index2.html')


def homeFromAdmin(request):
	return redirect('home')

# def adminlogin(request):
# 	return render(request, 'gmaps/adminLogin.html')

def routes(request):
	return render(request, 'gmaps/routes.html')


def routeDetailsAdd(request):
	return render(request, 'gmaps/routeDetails.html')

def registerUser(request):
	if request.method=='POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username=request.POST.get('username')
		email=request.POST.get('email')
		password1=passwordgenerator()
		role=request.POST.get('role')
		mobile=request.POST.get('mobile')
		check_user=User.objects.filter(email=email).first()
		check_profile=Registration.objects.filter(mobile=mobile).first()
		if check_user or check_profile:
			print("Insideee iffffffffffff")
			return render(request,'gmaps/registerAdmin.html')
		user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
		
		cont_obj = Registration(user = user, role = role,mobile=mobile)
		print(cont_obj)
		cont_obj.save()

		subject='user id and password'
		message=f'hi {user.username},your userid={user.username} and password={password1} login using them'
		email_from=settings.EMAIL_HOST_USER
		recipient_list=[user.email,]
		send_mail(subject,message,email_from,recipient_list)
		return render(request,'gmaps/registerAdmin.html') 
	return render(request,'gmaps/registerAdmin.html')		

def uloginpage(request):
	
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		# role  = request.POST.get('role')
		# user=authenticate(request,username=username,password=password)
		# if user is not None:
		# 	login(request,user)
		# 	return redirect('home')
		user = authenticate(request,username = username,password=password)
		if user is not None:
			login(request,user)
			return render(request,'gmaps/routeDetails.html')
            
			
	
	return render(request,'gmaps/adminLogin.html')

def loginUserandDriver(request):
	
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		role  = request.POST.get('role')
		print("role = ",role)
		val1 = 0
		val2 = 0
		if role == 'Student':
			val1 = 1
			user = auth.authenticate(username = username,password = password)
		elif role == 'Driver':
			val2 = 2
			user = auth.authenticate(username = username,password = password)
		else:
			user = None
		# user=authenticate(request,username=username,password=password)
		# if user is not None:
		# 	login(request,user)
		# 	return redirect('home')
		


		if user is not None:
			reg = Registration.objects.get(user = user)

			if int(reg.role) == val1:
				auth.login(request,user)
				return render(request,'gmaps/userHomePage.html')

			elif int(reg.role) == val2:
				auth.login(request,user)
				return render(request,'gmaps/mapSecond.html')



		# abc=Registration.objects.all()
		# xyz=abc.filter(username=username)
		# for i in xyz:
		# 	print(i.username)
		# 	if i.username == username and i.password==password and role == 'Student':
		# 		return render(request,'gmaps/userHomePage.html')
		# 	elif i.username == username and i.password==password and role == 'Driver':	
		# 		return render(request,'gmaps/mapSecond.html')
	return render(request,'gmaps/loginForUserandDriver.html')


def drv(request):
	number = request.POST.get('myNumber')
	print(number)
	data3 = database.child('users').get().val()
	data4=database.child('users').child(number).child('coords').child('latitude').get().val()
	data5=database.child('users').child(number).child('coords').child('longitude').get().val()
	
	print(data4)
	context={
	  "All":data3,
	  "latitude":data4,
	  "longitude":data5
	}
	return render(request,'gmaps/text.html',context)


def send_otp(mobile,otp):
	account_sid = 'AC7c348afa6c41036deab7d7d42a8cf154'
	auth_token  = '717a710de10ebb4aaf62a14877688369'
	client = Client(account_sid, auth_token)
	

	message = client.messages.create(
		    body='Your otp for login is'+otp,
		    to="+91"+ mobile,
		    from_="+12015375931"
		    )
	print (message.sid)

def loginwithphone(request):
	return render(request,'gmaps/loginwithphone.html')

def loginwithotp(request):
    if request.method=="POST":
    	mobile=request.POST.get('mobile')
    	role=request.POST.get('role')
    	request.session['role'] = role
    	user=Registration.objects.filter(mobile=mobile).first()
    	if user is None:
    		return render(request,'loginwithphone.html')
    	else:
    		otp = str(random.randint(1000 , 9999))
    	
    		print(otp)
    		request.session['otp'] = otp
    		send_otp(mobile,otp)	
    		return render(request,'gmaps/enterotp.html')

def enterotp(request):
	if request.method=="POST":
		otpget=request.POST.get('enterotp')
		otp =  request.session['otp']
		role = request.session['role']
		print(otpget)
		if otpget==otp:
			print("INside iffffffffffffffff")
			if role == 'Student':
				print("INside if")
				return render(request,'gmaps/userHomePage.html')
			elif role == 'Driver':
				return render(request,'gmaps/mapSecond.html')
		else:
			return render(request,'gmaps/enterotp.html')


			
		


	

def post_create(request):
    busnumber=request.POST.get('busno')	
    context={
        "busnum":busnumber
    }
    print(busnumber)
    idtoken=request.session['uid']
    a=authe.get_account_info(idtoken)
    print(str(a))
    a=a['users']
    a=a[0]
    a=a['localId']
    print("info"+str(a))

    data3=database.child('users').child(a).get().val()
    print(data3)

    return render(request,'gmaps/mapSecond.html')

def userHomePage(request):
	return render(request,'gmaps/userHomePage.html')

def findMyBus(request):
	request.session['latitude'] = 0
	request.session['longitude'] = 0
	if request.method=="POST":
		selectroute = request.POST.get("selectedroute")
		selectebuno=request.POST.get("selectedbusno")
		print(selectroute)
		
		a = Route.objects.get(routeno = selectroute)
		print(a)
		buses = Driverdetails.objects.all()
		print(buses)
		buss=buses.filter(selectroute=a)

		
		# print(selectedroute)
		
		
		print(buss)
		
		
		
		context = {
		 "selectroutes" : Route.objects.all(),
         "bus" : buss,
		}
		return render(request, 'gmaps/searchMyBus.html',context)

	context={
	  "Routes":Route.objects.all(),
	  "driverdetails":Driverdetails.objects.all()
	}
  #           "selectroutes" : Route.objects.all(),
  #           "bus" : buss,
  #       }
  #       return render(request, 'gmaps/searchMyBus.html', context=context)
 #    context = {

	#   "Routes":Routes

	# }

	return render(request,'gmaps/findMyBus.html',context=context)

def searchMyBus(request):

	return render(request,'gmaps/searchMyBus.html')

def getDetailsFromDB(request , busNo,dest):
	print(dest)
	data3 = database.child('users').get().val()
	for i in data3:
		if i == busNo:
			print(i)
			data4=database.child('users').child(i).child('coords').child('latitude').get().val()
			data5=database.child('users').child(i).child('coords').child('longitude').get().val()
	
	context ={
	"data4":data4,
	"data5":data5,
	"dest" : dest,
	"busNo":busNo,
	"role":"user"

	}
	return render(request,'gmaps/mapPage.html',context)

def eveningMap(request):
	return render(request,'gmaps/eveningMap.html')


def uregistrationpage(request):
	form=CreateUserForm()
	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
	context= {'form':form}		
	return render(request,'gmaps/userregistration.html',context)


def ulogout(request):
	auth.logout(request)
	return redirect('home')

def driverdetails(request):
	form2=Driverdetailsform()
	if request.method=='POST':
		form2=Driverdetailsform(request.POST)
		if form2.is_valid():
			form2.save()
			return redirect('/')
	context={'form2':form2}
	return render(request,'gmaps/adddriverdetails.html',context)


def Addroutes(request):
	# form1=Routeform()
	# if request.method=='POST':
	# 	form1=Routeform(request.POST)
	# 	if form1.is_valid():
	# 		form1.save()
	# 		return redirect('/')
	# context={'form1':form1}
	# return render(request,'gmaps/routes.html',context)
	if request.method=='POST':
		source1=request.POST.get('source')
		destination1=request.POST.get('destination')
		routeno1=request.POST.get('routeno')
		cont_obj = Route(source = source1, destination=destination1 , routeno = routeno1)
		print(cont_obj)
		cont_obj.save()

	return render(request,'gmaps/routeDetails.html')	


# def viewRoutes(request):
# 	if request.method=="POST":
# 		selectrouteno = request.POST.get('routeno')
# 		Routes = Route.objects.all()
# 		selectedno=Routes.filter(routeno=selectrouteno)
# 		context = {
#             "routess" : selectedno,
#         }
#         return render(request,'gmaps/routeDetails.html',context=context)

def viewRoutes(request):
	flag = 0
	if request.method == "POST":

		routeno = request.POST.get("routeno")
		Routes = Route.objects.all()
		selectedno = Routes.filter(routeno = routeno)
		context = {
		  "numbers":Route.objects.all(),
		  "routess":selectedno,
		  "flag":flag
		}
		return render(request, 'gmaps/routes.html',context = context)
	context = {
		  "demo":Route.objects.all(),
		  "flag":flag
	}

	return render(request, 'gmaps/routes.html',context = context)
       
# def showroutes(request):
# 	form3=Showroutesform()
# 	if request.method=='POST':
# 		form3=Showroutesform(request.POST)
# 		if form3.is_valid():
# 			form3.save()
# 			return redirect('/')
# 	context={'form3':form3}
# 	return render(request,'gmaps/showroutes.html',context)


def find(request):
    if request.method=="POST":
        selectroute = request.POST.get("route")
        buses = Driverdetails.objects.all()
        print(buses)
        buss=buses.filter(selectroute=selectroute)
               
        context = {
            "selectroutes" : Route.objects.all(),
            "bus" : buss,
        }
        return render(request, 'gmaps/showbus.html', context=context)
    context = {
        "selectroutes" : Route.objects.all(),
        "buses" : Driverdetails.objects.all(),

        
    }
    return render(request, 'gmaps/find.html', context=context)

def show(request):
	# routeno = request.POST.get("routeno")
	if request.method=="POST":
		flag = 1
		if request.POST.get('source'):
			InpRouteNumber = int(request.POST.get('letsgo'))
			Inpsource = request.POST.get('source')
			Inpdestination = request.POST.get('destination')

			a = Route.objects.filter(routeno = InpRouteNumber)
			a.update(source=Inpsource,destination=Inpdestination)



			return redirect(viewRoutes)
		else:
			answer = int(request.POST.get("letsgo"))
			selectrouteno = Route.objects.all()
			selectedno = selectrouteno.filter(routeno = answer)
			context={
			 "select":selectedno,
			 "flag":flag,
			}
			return render(request,'gmaps/routes.html',context=context)

def driverDetails(request):
	if request.method=='POST':
		driverName=request.POST.get('driverName')
		busNo=request.POST.get('busNo')
		selectedroute=int(request.POST.get('selectedroute'))
		# print(selectedroute)
		a = Route.objects.get(routeno = selectedroute)
		cont_obj = Driverdetails(busNo = busNo, driverName=driverName,selectroute=a)
		print(cont_obj)
		cont_obj.save()
	context = {
		"selectroute" : Route.objects.all(),
        
	}
	
	return render(request,'gmaps/updateDriverDetails.html',context)

def update_session(request):
	print("working")
	latitude = request.GET['latitude']
	longitude = request.GET['longitude']
	print("latitude:",latitude)
	print("longitude:",longitude)
	request.session['latitude']=latitude
	request.session['longitude']=longitude
	print(request.session['latitude'])
	print(request.session['longitude'])
	data = {}
	return JsonResponse(data)

def profile(request):
    if request.user.is_authenticated:
        return render(request,'gmaps/profile.html')
    else:
        return redirect(loginForUserandDriver) 

def update_marker(request):
	print("Update markerrr")
	busNo = request.GET['busNo']
	print(busNo)
	data3 = database.child('users').get().val()
	for i in data3:
		if i == busNo:
			print(i)
			data4=database.child('users').child(i).child('coords').child('latitude').get().val()
			data5=database.child('users').child(i).child('coords').child('longitude').get().val()
	
	data = {
	 "lat" :data4,
	 "long":data5
	}
	return JsonResponse(data)

def viewProfile(request):
	return render(request,'gmaps/profile.html')

def redirect_to_map(request):
	print("working")
	source = request.GET['source']
	destination = request.GET['destination']
	data = {
	 'source' : source,
	 'destination' : destination
	}
	return JsonResponse(data)

def viewProfileDriver(request):
	return render(request,'gmaps/profileForDriver.html')

def mapSec(request):
	return render(request,'gmaps/mapSecond.html')

def usercomplaint(request):
	if request.method=="POST":
	    name=request.POST.get('name')	
	    busno=request.POST.get('busno')
	    complaints=request.POST.get('complaints')
	    cont_obj = complaint(name = name, busno = busno,complaints=complaints)
	    cont_obj.save()
	    return render(request,'gmaps/emergency.html')
	return render(request,'gmaps/emergency.html')



def admincomplaint(request):
    getcomplaints=complaint.objects.all()
    context={"getcomplaints":getcomplaints}
    return render(request,'gmaps/usercomplaints.html',context)

def delete_complaint(request, pk):
	complaintss = complaint.objects.get(id=pk)
	print(complaintss)
	if request.method == "POST":
		complaintss.delete()
		getcomplaints=complaint.objects.all()
		context={"getcomplaints":getcomplaints}
		return render(request, 'gmaps/usercomplaints.html',context)
	context = {'comp':complaintss}
	return render(request, 'gmaps/delete.html', context)

def index(request):
	form=ImageForm()
	img=Image.objects.all()
	return render(request,"gmaps/images.html",{"img":img,"form":form})     
def index2(request):
	if request.method == "POST":
		form=ImageForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			obj=form.instance
			return render(request,"gmaps/uploadedImage.html",{"obj":obj})    

def shownotice(request):
	img=Image.objects.all()
	print(img)
	context={"imag":img}
	return render(request,"gmaps/shownotice.html",context)


	


