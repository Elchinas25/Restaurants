from django import forms

from .models import Item
from restaurants.models import RestaurantLocation

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = [
			'restaurant',
			'name',
			'contents',
			'excludes',
			'public'
		]

	def __init__(self, user=None, *args, **kwargs):
		print(kwargs)
		#print(kwargs.pop('pepeeldelapaca'))
		# c = user.__class__
		# us = c.objects.first()
		# qs = us.restaurantlocation_set.all()
		# print('Se viene: ', qs.first(), qs.last())
		super(ItemForm, self).__init__(*args, **kwargs)
		self.fields['restaurant'].queryset = RestaurantLocation.objects.filter(owner = user)