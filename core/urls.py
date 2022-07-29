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
    path('dash', index, name="index"),
    path('user_signup',user_signup,name="user_signup"),
    path('', contact_list, name="contact_list"),
    path('contact_edit', contact_edit, name="contact_edit"),
    path('contact', contact, name="contact"),
    path('save_contact', save_contact, name="save_contact"),
    path('update_contact', update_contact, name="update_contact"),
    path('delete_contact', delete_contact, name="delete_contact"),
    path('pipeline',pipeline,name="pipeline"),
    path('pipeline_add',pipeline_add,name="pipeline_add"),
    path('get_comp_details/', get_comp_details, name="get_comp_details"),
    path('get_contact_details/',get_contact_details, name="get_contact_details"),
    path('save_pipeline',save_pipeline, name="save_pipeline"),
    path('pipeline_edit',pipeline_edit, name="pipeline_edit"),
    path('update_pipeline',update_pipeline,name="update_pipeline"),
    path('delete_pipeline',delete_pipeline,name="delete_pipeline"),
    path('change_pipeline_status/',change_pipeline_status,name="change_pipeline_status"),




# Mobile-Api
    path('api/savecontact', SaveContact.as_view(), name='api/savecontact'),
    path('api/contactlist', ContactList.as_view(), name='api/contactlist'),
    path('api/getcontact/<id>', GetContact.as_view(), name='api/getcontact'),
    path('api/deletecontact/<id>', DeleteContact.as_view(), name='api/deletecontact'),
    path('api/updatecontact/<id>', UpdateContact.as_view(), name='api/updatecontact'),
    path('api/savepipeline', SavePipeline.as_view(), name='api/savepipeline'),
    path('api/pipelinelist', PipelineList.as_view(), name='api/pipelinelist'),
    path('api/getpipeline/<id>', GetPipeline.as_view(), name='api/getpipeline'),
    path('api/updatepipeline/<id>', UpdatePipeline.as_view(), name='api/updatepipeline'),
    path('api/deletepipeline/<id>', DeletePipeline.as_view(), name='api/deletepipeline'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
