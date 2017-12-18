from django.core.exceptions import ValidationError

#Validators only look for mistakes. You cannot change data. Do it in the signals

CATEGORIES = ['Ciegazo', 'Cancer', 'Postres', 'Japones', 'Chino', 'Pizza']

def validate_category(value):
	if not value in CATEGORIES and not value.capitalize() in CATEGORIES:
		raise ValidationError(f'{value} is not a valid category man. Try again')