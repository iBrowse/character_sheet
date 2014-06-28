from django.shortcuts import render
from django.http import HttpResponse
from .models import Character

def character_sheet(request):
	character_sheet = Character.objects.all()
	return render(request, "thisapp/charactersheet.html",{
		'character_sheet': character_sheet,
	})
