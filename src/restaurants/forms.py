from django import forms

from .models import RestaurantLocation

from .validators import validate_category

class RestaurantCreateForm(forms.Form):
	name 		= forms.CharField()
	location 	= forms.CharField(required=False)
	category	= forms.CharField(required=False) #Not necessary if you overwite it later in the ModelForm

class RestaurantLocationCreateForm(forms.ModelForm):
	#category = forms.CharField(required = False,  validators = [validate_category])
	class Meta:
		model = RestaurantLocation
		fields = [
			'name',
			'location',
			'category',
		]

	def __init__(self, user, *args, **kwargs):
		print(user)

