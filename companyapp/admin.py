from django.contrib import admin

from .models import About, Portfolio, Service, Slider

# Register your models here.
admin.site.register(Slider)
admin.site.register(About)
admin.site.register(Service)  
admin.site.register(Portfolio)  