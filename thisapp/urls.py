from django.conf.urls import patterns, url

from thisapp import views

urlpatterns = patterns('',
	url(r'^$', views.character_sheet, name='character_sheet')
)