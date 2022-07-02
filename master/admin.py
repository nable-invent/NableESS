from django.contrib import admin

# Register your models here.
from .models import Company, Individual, Pipeline

admin.site.register(Company)
admin.site.register(Individual)
admin.site.register(Pipeline)