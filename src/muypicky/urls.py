
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView #Solo necesitas el template

from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^items/', include('menus.urls', namespace='items')),
    url(r'^u/', include('profiles.urls', namespace='profiles')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name= "home.html"), name='home'),
    url(r'^login/$', LoginView.as_view(), name = 'login'),
    url(r'^about/$', TemplateView.as_view(template_name = "about.html"), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name = "contact.html"), name='contact'),
    #url(r'^restaurants/ciego$', CiegoRestaurantListView.as_view()),
    #url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    #url(r'^restaurants/sushi$', SushiRestaurantListView.as_view()),
]


