
from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from .models import propertyInfo



urlpatterns = [
    # url(r'^$', views.index, name='index'),

    # url(r'^(?P<pk>\d+)$', views.index, name='index'),



    # url(r'^$', ListView.as_view(queryset=propertyInfo.objects.all()[:25],
    #                                 template_name="getMortgage/home.html")),




    url(r'^logoutClass', views.logoutClass, name='logoutClass'),
]
