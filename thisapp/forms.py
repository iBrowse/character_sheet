from django import forms

class DiceForm(forms.Form):
	num_dice = forms.IntegerField(label="Number of Dice", min="1", max="20")
	num_sides = forms.IntegerField(label="Numer of Sides", min="4", max="100")
