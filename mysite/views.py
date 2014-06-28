from django.shortcuts import render

def home(request):
	return render(request,'templates/mysite/home.html')
