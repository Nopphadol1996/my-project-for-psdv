from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate ,login
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.

#def Home(request):
#    return HttpResponse('<h1> Hello World</h1>')

def Home(request):
	 

	posts = Post.objects.all()
	context = {"posts":posts}
 
	return render(request, 'maintenance/home.html',context)


def Sent_repair(request):
	# received from html
	if request.method == 'POST':
		data = request.POST.copy()
		title = data.get('title')
		work_order = data.get('work_order')
		serial = data.get('serial')
		station = data.get('station')
		bound = data.get('bound')
		equipment = data.get('equipment')
		detial = data.get('detial')
		sentrepairby = data.get('sentrepairby')
		orderid = data.get('orderid')
		# print(title,work_order,serial,station,bound,equipment,detial,sentrepairby)
		#mid = str(orderid).zfill(4) # zfill คือ การเติม 0 ด้านหน้า ไม่สามารถใช้กับ Integerได้ ต้องแปลงเป็น str ก่อน
		dt = datetime.now().strftime('%Y%m%d%H%M%S') # ทำหรัสจากวันที่เพื่อจะได้ไม่ให้ซ้ำกัน 
		orderid = 'OD' + dt # รวมกันเป็นรหัสID ที่ไม่ซ้ำกันแน่นอน
		
		# Save to model
		new = Work_request()
		new.orderid = orderid
		new.title = title
		new.work_order = work_order
		new.serial = serial
		new.station = station
		new.bound = bound
		new.equipment = equipment
		new.detial = detial
		new.sentrepairby = sentrepairby 
		new.save()
		return redirect('orders')

	return render(request,'maintenance/sentordertorepair.html')

def OrdersList(request):
	order = Work_request.objects.all().order_by('id').reverse()
	context = {'order':order}

	return render(request,'maintenance/order.html',context)

def UpdateStatusOrder(request,orderid,status):
	
	order  = Work_request.objects.get(orderid=orderid)
	if status == 'confirm':
		order.status =True
	elif status == 'cancel':
		order.status = False
	order.save()
	return redirect('orders')

def Posts(request):

	posts = Post.objects.all()
	context = {"posts":posts}

	return render(request, 'maintenance/blogs.html',context)

