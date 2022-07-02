from tkinter import N
from typing import Container
from django.db import models
from accounts.models import CustomUser
# Create your models here.
CONTACT_TYPES = [
    ("Individual","Individual"),
    ("Company","Company"),
]

class Company(models.Model):
    title = models.CharField(max_length=100, null=True)
    tax_id = models.CharField(max_length=100, null=True, blank=True)
    phone = models.BigIntegerField(null=True)
    mobile = models.BigIntegerField(null=True)
    email = models.EmailField(null=True)
    website = models.URLField(null=True)
    tags = models.CharField(max_length=100, null=True)
    company_image = models.FileField(null=True)
    address_street_1 = models.CharField(max_length=100, null=True)
    address_street_2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    internal_notes = models.TextField(null=True)
    internal_notes = models.TextField(null=True)
    sales_person = models.CharField(max_length=100, null=True)
    refrence = models.CharField(max_length=100,null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.title

class Individual(models.Model):
    title = models.CharField(max_length=100, null=True)
    company_name = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)
    tax_id = models.CharField(max_length=100, null=True, blank=True)
    address_street_1 = models.CharField(max_length=100, null=True)
    address_street_2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    individual_image = models.FileField(null=True)
    job_position = models.CharField(max_length=100, null=True)
    phone = models.BigIntegerField(null=True)
    mobile = models.BigIntegerField(null=True)
    email = models.EmailField(null=True)
    website = models.URLField(null=True)
    sr_title = models.CharField(max_length=100, null=True)
    tags = models.CharField(max_length=100, null=True)
    internal_notes = models.TextField(null=True)
    sales_person = models.CharField(max_length=100, null=True)
    refrence = models.CharField(max_length=100,null=True)
    industry = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)


    def __str__(self):
        return self.title



STATUS = [
    ("New","New"),
    ("Qualified","Qualified"),
    ("Propostion","Propostion"),
    ("Won","Won"),
]


class Pipeline(models.Model):
    contact = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)
    oppertunity = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.BigIntegerField(null=True)
    expected_revenue = models.IntegerField(null=True)
    rating = models.CharField(max_length=5, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.contact