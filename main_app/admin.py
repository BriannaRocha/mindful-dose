from django.contrib import admin
from .models import Drug, Dose

# Register your models here.
admin.site.register(Drug)
admin.site.register(Dose)