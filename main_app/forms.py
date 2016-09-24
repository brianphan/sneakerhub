from django import forms

class SneakerForm(forms.Form):
	name = forms.CharField(label='Name', max_length=100)
	brand = forms.CharField(label='Brand', max_length=100)
	price = forms.DecimalField(label='Price', max_digits=100, decimal_places=2)
	img_url = forms.CharField(label='Image URL', max_length=100)