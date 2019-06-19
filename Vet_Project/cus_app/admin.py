from django.contrib import admin
from .models import Pet, Customer, Visit, Photo
# Register your models here.

admin.site.register(Pet)
admin.site.register(Customer)
admin.site.register(Visit)
admin.site.register(Photo)
