from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html', {'sneakers': sneakers})

class Sneaker():
	def __init__(self, name, brand, price, img_url):
		self.name = name
		self.brand = brand
		self.price = price
		self.img_url = img_url


sneakers = [
	Sneaker("Adidas Ultra Boost Core Black White", "Adidas", 180.00, "https://s3.amazonaws.com/sneakerhub-project/sneaker_images/Adidas-Ultra-Boost-Core-Black-White.jpg"),
	Sneaker("Adidas Ultra Boost Triple White", "Adidas", 180.00, "https://s3.amazonaws.com/sneakerhub-project/sneaker_images/Adidas-Ultra-Boost-Triple-White.jpg"),
	Sneaker("Jordan 1 Retro BRED (2016)", "Jordan", 210.00, "https://s3.amazonaws.com/sneakerhub-project/sneaker_images/Jordan-1-Retro-BRED-(2016).jpg"),
	Sneaker("Jordan 2 Retro Just Don Blue", "Jordan", 650.00, "https://s3.amazonaws.com/sneakerhub-project/sneaker_images/Jordan-2-Retro-Just-Don-Blue.jpg"),
	Sneaker("Kobe 9 Elite Low Beethoven", "Adidas", 200.00, "https://s3.amazonaws.com/sneakerhub-project/sneaker_images/Nike-Kobe-9-Elite-Low-Beethoven.jpg"),
	Sneaker("Kobe 11 Elite Low Bruce Lee", "Adidas", 200.00, "https://s3.amazonaws.com/sneakerhub-project/sneaker_images/Nike-Kobe-11-Elite-Low-Bruce-Lee.jpg"),
]