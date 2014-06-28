from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Character, Games

def home(request):
	game_list = Games.objects.all()
	return render(request, "thisapp/home.html", {
		'game_list': game_list,
	})

def roll_dice(request):
	if request.method == 'POST':
		form = RollDiceForm(requst.POST)
		if form.is_valid():
			return HttpResponseRedirect(reverse("home"))
	else:
		form = RollDiceForm()
	return render(request, 'home.html',{'form': form})

def character_sheet(request):
	character_sheet = Character.objects.all()
	return render(request, "thisapp/charactersheet.html",{
		'character_sheet': character_sheet,
	})
