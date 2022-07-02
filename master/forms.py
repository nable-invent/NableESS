from .models import Company, Individual
from django import forms





class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = "__all__"