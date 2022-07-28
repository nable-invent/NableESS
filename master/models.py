from tkinter import N
from typing import Container
from django.db import models
from accounts.models import CustomUser
from core.settings import COMPANY_IMAGE,INDIVIDUAL_IMAGE
# Create your models here.

CONTACT_TYPES = [
    ("Individual","Individual"),
    ("Company","Company"),
]


class Company(models.Model):
    name = models.CharField(max_length=100, null=True)
    tax_id = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50,null=True,blank=True)
    mobile = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    tags = models.CharField(max_length=100, null=True,blank=True)
    image = models.FileField(default=COMPANY_IMAGE,upload_to='company_image/',null=True,blank=True)
    address_street_1 = models.CharField(max_length=100, null=True,blank=True)
    address_street_2 = models.CharField(max_length=100, null=True,blank=True)
    city = models.CharField(max_length=50, null=True,blank=True)
    state = models.CharField(max_length=100, null=True,blank=True)
    country = models.CharField(max_length=100, null=True,blank=True)
    zip_code = models.CharField(max_length=100, null=True,blank=True)
    internal_notes = models.TextField(null=True,blank=True)
    sales_person = models.CharField(max_length=100, null=True,blank=True)
    refrence = models.CharField(max_length=100,null=True,blank=True)
    industry = models.CharField(max_length=100, null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.name)

class Individual(models.Model):
    name = models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=100, null=True,blank=True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    tax_id = models.CharField(max_length=100, null=True, blank=True)
    address_street_1 = models.CharField(max_length=100, null=True,blank=True)
    address_street_2 = models.CharField(max_length=100, null=True,blank=True)
    city = models.CharField(max_length=50, null=True,blank=True)
    state = models.CharField(max_length=100, null=True,blank=True)
    country = models.CharField(max_length=100, null=True,blank=True)
    zip_code = models.CharField(max_length=100, null=True,blank=True)
    image = models.FileField(default=INDIVIDUAL_IMAGE,upload_to='individual_image/',null=True,blank=True)
    job_position = models.CharField(max_length=100, null=True,blank=True)
    phone = models.CharField(max_length=50,null=True,blank=True)
    mobile = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    # sr_title = models.CharField(max_length=100, null=True,blank=True)
    tags = models.CharField(max_length=100, null=True,blank=True)
    internal_notes = models.TextField(null=True,blank=True)
    sales_person = models.CharField(max_length=100, null=True,blank=True)
    refrence = models.CharField(max_length=100,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    

    def __str__(self):
        return self.name


class Contact(models.Model):
    cmp_title = models.CharField(max_length=100, null=True)
    cmp_tax_id = models.CharField(max_length=100, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True,blank=True,related_name='company_type_id')
    cmp_phone = models.CharField(max_length=50,null=True,blank=True)
    cmp_mobile = models.CharField(max_length=50,null=True,blank=True)
    cmp_email = models.EmailField(null=True,blank=True)
    cmp_website = models.URLField(null=True,blank=True)
    cmp_tags = models.CharField(max_length=100, null=True,blank=True)
    company_image = models.FileField(default=COMPANY_IMAGE,upload_to='company_image/',null=True,blank=True)
    cmp_address_street_1 = models.CharField(max_length=100, null=True,blank=True)
    cmp_address_street_2 = models.CharField(max_length=100, null=True,blank=True)
    cmp_city = models.CharField(max_length=50, null=True,blank=True)
    cmp_state = models.CharField(max_length=100, null=True,blank=True)
    cmp_country = models.CharField(max_length=100, null=True,blank=True)
    cmp_zip_code = models.CharField(max_length=100, null=True,blank=True)
    cmp_internal_notes = models.TextField(null=True,blank=True)
    cmp_sales_person = models.CharField(max_length=100, null=True,blank=True)
    cmp_refrence = models.CharField(max_length=100,null=True,blank=True)
    cmp_industry = models.CharField(max_length=100, null=True,blank=True)
    
    name = models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=100, null=True,blank=True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, null=True,related_name='company_name',blank=True)
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE, null=True,blank=True)
    tax_id = models.CharField(max_length=100, null=True, blank=True)
    address_street_1 = models.CharField(max_length=100, null=True,blank=True)
    address_street_2 = models.CharField(max_length=100, null=True,blank=True)
    city = models.CharField(max_length=50, null=True,blank=True)
    state = models.CharField(max_length=100, null=True,blank=True)
    country = models.CharField(max_length=100, null=True,blank=True)
    zip_code = models.CharField(max_length=100, null=True,blank=True)
    individual_image = models.FileField(default=INDIVIDUAL_IMAGE,upload_to='individual_image/',null=True,blank=True)
    job_position = models.CharField(max_length=100, null=True,blank=True)
    phone = models.CharField(max_length=50,null=True,blank=True)
    mobile = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    # sr_title = models.CharField(max_length=100, null=True,blank=True)
    tags = models.CharField(max_length=100, null=True,blank=True)
    internal_notes = models.TextField(null=True,blank=True)
    sales_person = models.CharField(max_length=100, null=True,blank=True)
    refrence = models.CharField(max_length=100,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        if self.cmp_title == None:
            return self.name
        else:
            return self.cmp_title


STATUS = [
    ("New","New"),
    ("Qualified","Qualified"),
    ("Propostion","Propostion"),
    ("Won","Won"),
]


class Pipeline(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    opportunity = models.CharField(max_length=100, null=True,blank=True)
    email = models.EmailField(max_length=100, null=True,blank=True)
    phone = models.BigIntegerField(null=True,blank=True)
    expected_revenue = models.FloatField(max_length=50 ,null=True,blank=True)
    rating = models.CharField(max_length=5, null=True,blank=True)
    status = models.CharField(max_length=100, null=True, default="New",choices=STATUS,blank=True)

    def __str__(self):
        return str(self.contact)