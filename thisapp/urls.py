from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from thisapp import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^character/', views.character_sheet, name="character_sheet"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
