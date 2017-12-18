from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL

# Create your models here.
class RestaurantLocation(models.Model):
	owner 		= models.ForeignKey(User) #To get the associated objts: class_instance(of class contrib...).modelminuculas_set.all()
	name 		= models.CharField(max_length=120)
	location 	= models.CharField(max_length=120, null=True, blank=True)
	category	= models.CharField(max_length=120, null=True, blank=True,  validators = [validate_category])
	slug 		= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('restaurants:detail', kwargs={'slug': self.slug})
		#return f"/restaurants/{self.slug}"

	@property
	def title(self):
		return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	print('Saving eyou hacker...')
	print(instance.name)
	instance.category = instance.category.capitalize()
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender = RestaurantLocation)
#post_save.connect(rl_post_save_reciever, sender = RestaurantLocation)

# def rl_post_save_reciever(sender, instance, created, *args, **kwargs):
# 	print('Saved')
# 	print(instance.category)