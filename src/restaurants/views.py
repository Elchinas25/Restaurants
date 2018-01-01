from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.db.models import Q

from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


import random
# Create your views here.

# def restaurant_detailview(request, slug): #This returns the same as the class
# 	template_name = 'restaurants/restaurantlocation_detail.html'
# 	obj = RestaurantLocation.objects.get(slug=slug)
# 	context = {
# 	'object': obj
# 	}
# 	return render(request, template_name, context)


# @login_required(login_url='/login/')
# def restaurant_createview(request):
# 	form = RestaurantLocationCreateForm(request.POST or None)
# 	errors = None
# 	if form.is_valid():
# 		if request.user.is_authenticated():
# 			instance = form.save(commit=False)
# 			instance.owner = request.user
# 			form.save()
# 			return HttpResponseRedirect('/restaurants/')
# 		else:
# 			return HttpResponseRedirect('/restaurants/')
# 	if form.errors:
# 		errors = form.errors
# 	template_name = 'restaurants/form.html'
# 	context = {
# 		'form': form,
# 		'errors': errors
# 	}
# 	return render(request, template_name, context)

class RestaurantListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner = self.request.user)

	# def get_queryset(self):
	# 	slug = self.kwargs.get("slug")
	# 	if slug:
	# 		queryset = RestaurantLocation.objects.filter(
	# 			Q(category__iexact = slug) |
	# 			Q(category__icontains = slug)
	# 			)
	# 	else:
	# 		queryset = RestaurantLocation.objects.all()

class RestaurantDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner = self.request.user)

	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(RestaurantLocation, id=rest_id)
	# 	return obj

class RestaurantCreateView(LoginRequiredMixin, CreateView):
	login_url = '/login/'
	form_class = RestaurantLocationCreateForm
	template_name = 'form.html'
	#success_url = '/restaurants/'

	def form_valid(self, form):
		instance = form.save(commit = False)
		instance.owner = self.request.user
		return super(RestaurantCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add restaurant'
		return context

	# def get_form_kwargs(self):
	# 	kwargs = super(RestaurantCreateView, self).get_form_kwargs()
	# 	kwargs['user'] = self.request.user

	# def get_form_kwargs(self):
	# 	kwargs = super(RestaurantCreateView, self).get_form_kwargs()
	# 	kwargs['user'] = self.request.user
	# 	return kwargs


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	login_url = '/login/'
	form_class = RestaurantLocationCreateForm
	template_name = 'restaurants/detail-update.html'
	#success_url = '/restaurants/'

	# def get_queryset(self):
	# 	#qs = super(RestaurantUpdateView, self).get_queryset()
	# 	qs = RestaurantLocation.objects.all()
	# 	return qs

	# No need of def form_valid bc the form has already been created and is already valid

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
		name = self.object.name
		context['title'] = f'Editing restaurant: {name}'
		return context

	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner = self.request.user)

	def get_form_kwargs(self):
		kwargs = super(RestaurantUpdateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs







# def restaurant_listview(request):
# 	template_name = 'restaurants/restaurants_list.html'
# 	queryset = RestaurantLocation.objects.all()
# 	context = {
# 	"object_list": queryset
# 	}
# 	return render(request, template_name, context)





#class ContactView(TemplateView):
#	pass
	#template_name = "contact.html" || NO HACE FALTA



#class AboutView(TemplateView):
#	pass
	#template_name = "about.html"



# class HomeView(TemplateView):
# 	template_name = "home.html"
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(HomeView, self).get_context_data(*args, **kwargs)
# 		num = random.randint(1,1000000)
# 		pepe = ['Maria', 'Jesus']
# 		pares = [1, 2, 3, 4, 5, 6]
# 		var_entorno = True
# 		context = {
# 		"varr_entorno": var_entorno,
# 		"num": num,
# 		"pares": pares,
# 		"pepe": pepe,
# 		}
# 		return context
