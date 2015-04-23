from django.conf.urls import patterns, include, url

from soapws import views

urlpatterns = patterns('',

    url(r'^showusers', views.showusers,),
    url(r'^createuser', views.createuser,),
    url(r'^getuser/(?P<username>.+)/$', views.getuser,),
)
