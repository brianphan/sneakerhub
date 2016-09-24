from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Sneaker
from .forms import SneakerForm

# Create your views here.
def index(request):
	sneakers = Sneaker.objects.all()
	form = SneakerForm()
	return render(request, 'index.html', {'sneakers': sneakers, 'form': form})

def detail(request, sneaker_id):
	sneaker = Sneaker.objects.get(id=sneaker_id)
	return render(request, 'detail.html', {'sneaker': sneaker})

def post_sneaker(request):
	form = SneakerForm(request.POST, request.FILES)
	if form.is_valid():
		form.save(commit = True)

	return HttpResponseRedirect('/')