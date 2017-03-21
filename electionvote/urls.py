from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.redirect, name='redirect'),
	url(r'^dashboard/$', views.list, name='list'),
	url(r'^submit/$', views.submit, name='submit'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
]
