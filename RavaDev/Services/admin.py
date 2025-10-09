from django.contrib import admin

# Register your models here.
from .models import Service, Field
admin.site.register(Service)
admin.site.register(Field)