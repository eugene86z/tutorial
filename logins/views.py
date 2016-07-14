from django.shortcuts import render

# def index(request):
# 	return render(request, 'logins/home.html')




# from forms import LoginForm

def index(request):
	return render(request, 'logins/home.html')
	# if request.POST:
	# 	form = LoginForm(request.POST)


def mortgageLogin(request):
	return render(request, 'logins/mortLogin.html')


def mortLoginClick(request):
	print ('test')
	return render(request, 'logins/mortLogin.html')