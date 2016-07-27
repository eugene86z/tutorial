from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect
# from logins.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, loginForm
from django.contrib import auth



def index(request):
	return render(request, 'logins/home.html')
	# if request.POST:
	# 	form = LoginForm(request.POST)


def mortgageLogin(request):
	return render(request, 'logins/mortLogin.html')




def logoutClass(request):
	auth.logout(request)
	return HttpResponseRedirect('/logins/')







#LOGIN  -  GET MORTGAGE

class loginFormView(View):
	form_class = loginForm
	template_name =  'logins/mortLogin.html'



	# display blank form
	def get(self, request):
		form = self.form_class(None)  # self is the userForm
		return render(request, self.template_name, {'form': form})




	# process form data
	def post(self, request):

		form = self.form_class(request.POST) #keep getting form not valid if username exists


		if form.is_valid:

			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					print ('active')
					login(request, user)
					# m = Member.objects.get(user)
					# request.session['member_id']
					return HttpResponseRedirect('/getMortgage/')
				else:
					print('disabled account')
					# Return a 'disabled account' error message
			else:
				print ('invalid login')

		else:
			print ('invalid form') #why


		return render(request, self.template_name, {'form': form})










#REGISTRATATION  -  GET MORTGAGE

class UserFormView(View):
	form_class = UserForm
	template_name =  'logins/registration_form_getMortgage.html'

	#display blank form
	def get(self, request):
		form = self.form_class(None) #self is the userForm
		return render(request, self.template_name, {'form':form})


	# process form data
	def post(self, request):
		# print ('test')
		form = self.form_class(request.POST)

		if form.is_valid():  #no weird characters..

			user = form.save(commit=False) #diesn't save it yet, perform checks..

			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user.set_password(password)
			user.save()


			#return User objects if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None: # if found user and authenticated, user will now be username

				if user.is_active:  #checks for blocked users
					login(request, user) #logs user in
					#request.user.username  #to access that field
					return redirect('mainPage:index')

		return render(request, self.template_name, {'form': form})