from dataclasses import field, fields
from .models import Company, Individual,Pipeline
from django import forms



class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['address_street_1','address_street_2',
        'city','state','zip_code','country','tax_id','phone','mobile','email','website','title','tags']

class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields =  ['name','address_street_1','address_street_2',
        'city','state','zip_code','country','tax_id','job_position','phone','mobile','email','website','title','tags']


class PipelineForm(forms.ModelForm):
    class Meta:
        model = Pipeline
        fields = "__all__"