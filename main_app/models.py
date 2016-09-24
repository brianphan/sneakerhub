from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Sneaker(models.Model):
	name = models.CharField(max_length=100)
	brand = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=100, decimal_places=2)
	image = models.ImageField(upload_to='sneaker_images', default='media/default.png')

	def __str__(self):
		return self.name