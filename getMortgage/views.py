from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponseRedirect


def index(request):

	##check if logged in
	if request.user.is_authenticated():
		userName = request.user.username
		# print (userName)
		return render(request, 'getMortgage/home.html')
	else:
		return HttpResponseRedirect("/logins/mortLoginClick")



def logoutClass(request):
	auth.logout(request)
	return HttpResponseRedirect("/logins/mortLoginClick")