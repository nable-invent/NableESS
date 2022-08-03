from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
import datetime
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=True, unique=True)
    first_name = models.CharField(max_length=50,null=True, verbose_name="First Name ")
    last_name = models.CharField(max_length=50, null=True, verbose_name="Last Name ")
    date_joined = models.DateTimeField(default=datetime.datetime.now)
    phone_number = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Phone Number ", help_text="Optional")
    address = models.CharField(max_length=150,null=True, blank=True, verbose_name="Address")
    profile_image = models.ImageField(null=True, blank=True, upload_to ="profile image" ,verbose_name="Profile Image")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "All Users"
        verbose_name_plural = "All Users"

    def __str__(self):
        return f"{self.email}"