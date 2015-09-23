from django.shortcuts import render
# from django.contrib.auth.models import User
from users.models import User,UserProfile
from django.template import RequestContext
import random
import string
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
from django.contrib import auth
# Create your views here.

def home(request):
	# user = User.objects.all()
	# user.delete()
	# userprofile = UserProfile.objects.all()
	# userprofile.delete()
	return render(request,"signup.html")
def signup(request):
	if request.method== "POST":
		fname = request.POST.get("fname")
		lname = request.POST.get("lname")
		email = request.POST.get("email")
		user = User()
		user.first_name = fname
		user.last_name = lname
		user.email = email
		user.username = email
		user.save() 
		userprofile = UserProfile()
		random_str = (''.join(random.choice(string.ascii_uppercase) for i in range(12)))
		userprofile.user_id = user.id
		userprofile.temp_code = random_str
		userprofile.save()
		print userprofile.temp_code
		print settings.EMAIL_HOST_USER
		html_content = 'Set Password Link : ' + 'http://localhost:8000/users/set_pwd/'+userprofile.temp_code+''
		send_mail("Set Password", html_content, settings.EMAIL_HOST_USER,[email])
	return render(request,"mailsent.html")

def set_pwd(request,code):
	print code
	authenticated = True
	try:
		num = UserProfile.objects.filter(temp_code=code).count()
	except UserProfile.DoesNotExist:
		pass
		
	
	if request.method == 'POST':

		if(request.POST['pwd']):
			authenticated = False
		up = UserProfile.objects.get(temp_code=code)
		num_results = User.objects.get(id = up.user_id)
		if(num_results):
			u = User.objects.get(id=up.user_id)
			num_results.set_password(request.POST['pwd'])
			num_results.save()
			authenticated = True
			u_p = UserProfile.objects.get(user_id=u.id)
			u_p.temp_code=''
			u_p.save()
		return HttpResponseRedirect('/users/login/')
	return render(request,'set_pwd.html',{'temp_code':code})

def login(request):
	if request.method == "POST":
		username = request.POST['email']
		password = request.POST['pwd']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request,user)
				return HttpResponseRedirect('/users/home/')
	return render(request,"login.html")

def user_home(request):
	print request.user
	try:
		u = User.objects.get(id = request.user.id)
		if u:
			return render(request,"home.html")
	except:
		return HttpResponseRedirect('/users/login/')
	

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/users/login/')

	