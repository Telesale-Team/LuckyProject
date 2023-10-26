from django.shortcuts import render

# New import
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def Profile (request ):	

	user_profile = User.objects.all()
	
	context = {
		'user_profile': user_profile,
	}
	return render(request,'html_user/user.html',context)



def Edite_Profile (request,id):

	user_profile = User.objects.get(pk=id)

	context = {
		'user':user_profile,
	}
	return render(request,'html_user/user.html',context)