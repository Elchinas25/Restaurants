"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView #Solo necesitas el template

from django.contrib.auth.views import LoginView

#from restaurants.views import ContactView, HomeView, AboutView
from restaurants.views import (
    RestaurantCreateView,
)

urlpatterns = [
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^items/', include('menus.urls', namespace='items')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name= "home.html"), name='home'),
    url(r'^login/$', LoginView.as_view(), name = 'login'),
    url(r'^about/$', TemplateView.as_view(template_name = "about.html"), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name = "contact.html"), name='contact'),
    #url(r'^restaurants/ciego$', CiegoRestaurantListView.as_view()),
    #url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    #url(r'^restaurants/sushi$', SushiRestaurantListView.as_view()),
]

