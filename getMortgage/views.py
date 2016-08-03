from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from .models import propertyInfo
from django.template import RequestContext


def index(request):

	##check if logged in
	if request.user.is_authenticated():
		userName = request.user.username

		p = propertyInfo.objects.filter(userName=userName)


		return render(request, 'getMortgage/home.html',
								  {'categories':p})

	else:
		return HttpResponseRedirect("/logins/mortLoginClick")




def logoutClass(request):
	auth.logout(request)
	return HttpResponseRedirect("/logins/mortLoginClick")