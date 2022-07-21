"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from master.views import *
from mobile_api.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contact_list, name="contact_list"),
    path('contact_edit', contact_edit, name="contact_edit"),
    path('contact', contact, name="contact"),
    path('dash', index, name="index"),
    path('save_contact', save_contact, name="save_contact"),
    path('update_contact', update_contact, name="update_contact"),
    path('delete_contact', delete_contact, name="delete_contact"),
    path('pipeline',pipeline,name="pipeline"),
    path('get_comp_details/', get_comp_details, name="get_comp_details"),
    path('get_contact_details/',get_contact_details, name="get_contact_details"),
    path('save_pipeline',save_pipeline, name="save_pipeline"),

    path('api/savecontact', SaveContact.as_view(), name='api/savecontact'),
    path('api/savepipeline', SavePipeline.as_view(), name='api/savepipeline'),
    path('api/contactlist', ContactList.as_view(), name='api/contactlist'),
    path('api/getcontact/<id>', GetContact.as_view(), name='api/getcontact'),
    path('api/deletecontact/<id>', DeleteContact.as_view(), name='api/deletecontact'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
