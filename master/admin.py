from django import views
from django.contrib import admin

# Register your models here.
from .models import Company, Individual, Pipeline, Contact

class CompanyAdmin(admin.ModelAdmin):
    list_display = ["title"] 


admin.site.register(Company,CompanyAdmin)
admin.site.register(Individual)
admin.site.register(Pipeline)
admin.site.register(Contact)

