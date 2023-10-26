from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime

import random
from .models import *
from .forms import *
import qrcode

now = datetime.now()
formatted = now.strftime("%d/%m/%Y")




def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="black", back_color="white")
    return qr_code

def Home (request):


	random_number = str(random.randrange(300,600))
	round = Round.objects.all().filter(name=2)

	print(round)
	qr_code = generate_qr_code(str(random_number))
	#qr_code.save('QR-'+str(random_number))

	#print(len(random_number))


	if len(random_number) == 2:
		number = str(0) + random_number
		data = Data.objects.all()[int(number)]

		#print('ตัวเลข 2 ตัว ',random_number)
		print(data)


		context = {'data':data,'round':round}
		return render(request, 'html_index/home.html',context)
	
	elif len(random_number) == 1:		
		number = str(0)+ str(0) + random_number
		#data = Round_Tauthong(round=1,member='A112',number="002")
		#data.save()		
		data = Data.objects.all()[int(number)]
		print(data)

		context = {'data':data,'round':round}
		#print('ตัวเลข 1 ตัว ',random_number)
		return render(request, 'html_index/home.html',context)
	
	else:
		
		data = Data.objects.all()[int(random_number)]
		print(data)
		#print(random_number)
		#data = Round_Tauthong(round=1,member='A112',number="003")
		#data.save()

		context = {'data':data,'round':round}				
		return render(request, 'html_index/home.html',context)



def Lucky_Random (request):

	# Create a list of formatted numbers in the format "000-999"
	data = Data.objects.all()
	round = Round_Tauthong.objects.all()[:1]
	print(round)
	'''
	numbers = [f"{i:03d}" for i in range(1000)]

	for i in numbers:
		data = Data(no=i)
		print(data)
		print("--------")
		data.save()
	'''

	# Pass the list of numbers to the template
	context = {'data':data,'round':round}

	return render(request, 'html_index/datatable.html',context)


def Import_data (request):

	datas = Data.objects.all()

	context = {
		'Data':datas,
	}
	return render (request,'html_index/import.html',context)



def Add_Reward (request,no):

	round = Round.objects.filter(name=2)
	data = Data.objects.filter(no=no)

	context = {

		'data':data,
		'round':round,
	}

	return render (request,'html_index/add_reward.html',context)

def Save(request):

	if request.method == 'POST':
		form_data = Form_Import_Data(request.POST)
		if form_data.is_valid():
			form_data.save()
			return redirect ('add-reward')
		else:
			form_data()
			
	else:
		return render (request,'html_index/add_reward.html')
