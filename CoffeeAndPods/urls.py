
from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^coffee_machines$', coffee_machines_products),
    url(r'^coffee_pots$', coffee_pots_products),
]
