from django.db import models

class Character(models.Model):
	'''
	Responsible for character database structure
	'''
	name = models.CharField(primary_key=True, max_length=50)
	char_class = models.CharField(max_length=50)
	char_skills = models.TextField()
	char_story = models.TextField()

	#Traits
	brawn = models.IntegerField(default=1)
	finesse = models.IntegerField(default=1)
	wits = models.IntegerField(default=1)
	resolve = models.IntegerField(default=1)
	panache = models.IntegerField(default=1)

	
