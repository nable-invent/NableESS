from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django.contrib.auth import get_user_model
from django import forms

from .models import CustomUser

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name','last_name','email','phone_number','address','profile_image')
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'input--style-4','pattern':'[a-zA-Z]+','title':'Only Letters is Allow', 'required':'required','autofocus':'autofocus'}),
            'last_name':forms.TextInput(attrs={'class':'input--style-4','pattern':'[a-zA-Z]+','title':'Only Letters is Allow'}),
            'email':forms.EmailInput(attrs={'class':'input--style-4','type':'email','required':'required'}),
            'phone_number':forms.NumberInput(attrs={'class':'input--style-4','type':'tel','pattern':'[0-9]{10}','title':'Please Enter Valid Mobile Number'}),
            'address':forms.Textarea(attrs={'class':'input--style-4','rows':'1','cols':'22'}),
            'profile_image':forms.FileInput(attrs={'class':'input--style-4'}),

        }


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomPasswordResetForm(PasswordResetForm):
    class meta:
        model = CustomUser
        fields = ('email',)