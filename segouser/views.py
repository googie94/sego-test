from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Segouser

# Create your views here.

def home(request):
	user_id = request.session.get('user')
	if user_id:
		segouser = Segouser.objects.get(pk=user_id)
		return HttpResponse(segouser.username)
	
	return HttpResponse('home!')

def logout(request):
	if request.session.get('user'):
		del(request.session['user'])

	return HttpResponse('home!')


def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	elif request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		res_data={}
		if not (username and password):
			res_data['error'] = '모든 값을 입력해야 합니다.'
		else:
			segouser = Segouser.objects.get(username=username)
			if password == segouser.password:
				request.session['user'] = segouser.id
				return redirect('/home/')
			else:
				res_data['error'] = segouser.password, password

		return render(request, 'login.html', res_data)

def register(request):
	if request.method == 'GET':
		return render(request, 'register.html')
	elif request.method == 'POST':
		username = request.POST.get('username', None)
		email = request.POST.get('email', None)
		password = request.POST.get('password', None)
		rePassword = request.POST.get('rePassword', None)

		res_data={}
		if not (username and email and password and rePassword):
			res_data['error'] = '모든 값을 입력해야 합니다.'
		elif password != rePassword:
			res_data['error']='비밀번호 미일치!'
		else:
			user = Segouser(
				username=username,
				email=email,
				password=password,
			)
			res_data['error']=user.password

			user.save()

		return render(request, 'register.html', res_data)