from django.shortcuts import render

# Create your views here.
def index(request):
	name = 'Jordan 1 Retro BRED (2016)'
	price = 210.00
	context = {'name': name, 'price': price}
	return render(request, 'index.html', context)

