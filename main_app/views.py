from django.shortcuts import render
from .models import Sneaker

# Create your views here.
def index(request):
	sneakers = Sneaker.objects.all()
	return render(request, 'index.html', {'sneakers': sneakers})



