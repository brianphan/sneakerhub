from django import forms
from .models import Sneaker

class SneakerForm(forms.ModelForm):
	class Meta:
		model = Sneaker
		fields = ['name', 'brand', 'price', 'image']