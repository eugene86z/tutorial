
from django.conf.urls import url, include
from .import views
from django.views.generic import ListView, DetailView
from .models import propertyInfo



urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = propertyInfo,
                                             template_name = 'getMortgage/editPropInfo.html')),



    url(r'^logoutClass', views.logoutClass, name='logoutClass'),
]
