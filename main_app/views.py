from django.shortcuts import render
from .models import Sneaker

# Create your views here.
def index(request):
	sneakers = Sneaker.objects.all()
	return render(request, 'index.html', {'sneakers': sneakers})

def detail(request, sneaker_id):
	sneaker = Sneaker.objects.get(id=sneaker_id)
	return render(request, 'detail.html', {'sneaker': sneaker})

