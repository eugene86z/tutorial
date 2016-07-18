
from django.conf.urls import url, include
from . import views




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mortgageLogin$', views.mortgageLogin, name='mortgageLogin'),
    url(r'^mortLoginClick', views.mortLoginClick, name='mortLoginClick'),
    # url(r'^$', views.mortgageLogin, name='mortgageLogin'),
    url(r'^register/$', views.UserFormView.as_view(), name='register')
]
