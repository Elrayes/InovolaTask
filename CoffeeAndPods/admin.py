from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CoffeeMachines)
admin.site.register(CoffeePot)
admin.site.register(CoffeeFlavor)
admin.site.register(CPProductType)
admin.site.register(CMProductType)
admin.site.register(PackSize)

