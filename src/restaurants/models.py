from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from django.db.models import Q

from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL

class RestaurantLocationQuerySet(models.query.QuerySet):
	def search(self, query):
		if query:
			return self.filter(
				Q(name__icontains=query)|
				Q(category__icontains=query)|
				Q(location__icontains=query)|
				Q(item__name__icontains=query)|
				Q(item__contents__icontains=query)
				).distinct()
		else:
			return self.all()

class EverywhereLocation(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(location__iexact='Everywhere')

class RestaurantLocationManager(models.Manager):
	def get_queryset(self):
		return RestaurantLocationQuerySet(self.model, using=self.db)

# class RestaurantLocationManager(models.Manager):
# 	def get_queryset(self, name_user, query):
# 		super(RestaurantLocationManager, self).get_queryset().filter(name_user, query)
# 		user_pre_qs = self.filter(owner__icontains=name_user)
# 		return user_pre_qs.filter(
# 			Q(name__icontains=query)|
# 			Q(category__icontains=query)|
# 			Q(location__icontains=query)|
# 			Q(item__name__icontains=query)
# 			).distinct()


class RestaurantLocation(models.Model):
	owner 		= models.ForeignKey(User) #To get the associated objts: class_instance(of class contrib...).modelminuculas_set.all()
	name 		= models.CharField(max_length=120)
	location 	= models.CharField(max_length=120, null=True, blank=True)
	category	= models.CharField(max_length=120, null=True, blank=True,  validators = [validate_category])
	slug 		= models.SlugField(null=True, blank=True)

	objects = RestaurantLocationManager() #For RL.objects.whatevermethod()
	everywhere = EverywhereLocation()

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