
from cmath import e
from email.policy import default
from errno import EFAULT
from tkinter import N
from tkinter.messagebox import NO
from tokenize import Name
from django.shortcuts import redirect, render
from .forms import CompanyForm, IndividualForm,Company,Individual
from .models import Contact,Pipeline
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from . serializer import CompanySerializer,ContactSerializer
# Create your views here.


def index(request):
    return render(request, 'login.html')

# def company(request):
#     if request.method == 'POST':
#         form = CompanyForm(request.POST, request.FILES)
#         print("form", form)
#         if form.is_valid():
#             form.save()
#     form = CompanyForm()
#     context = {
#         "form":form,
#     }
#     return render(request, 'contactt.html', context)


def contact(request):
    return render(request, 'contact.html',{"data1":Company.objects.all()})


def save_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company_name = request.POST.get('company_name')
        street1 = request.POST.get('address_street_1')
        street2 = request.POST.get('address_street_2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip_code')
        country = request.POST.get('country')
        tax_id = request.POST.get('tax_id')
        job_position = request.POST.get('job_position') 
        phone = request.POST.get('phone',0) 
        mobile = request.POST.get('mobile',0) 
        email = request.POST.get('email') 
        website = request.POST.get('website') 
        title = request.POST.get('title') 
        tags = request.POST.get('tags') 
        image = request.FILES.get('image')
        user_type = request.POST.get('user_type',False)
        print(user_type)
        if user_type == "indivisual":
            if company_name == 'Select Company':
                return render(request,'contact.html',{"error":"Please Select Company Name","data1":Company.objects.all()})
            else:
                var = Company.objects.get(id=company_name)
                #form = IndividualForm(request.POST,request.FILES,None)
                print(name,company_name,street1,street2,city,state,zip,country,tax_id,job_position,phone,mobile,email,website,title,tags,image)
                try:
                    Individual(name=name,title=title,company_name=var,tax_id=tax_id,address_street_1=street1,address_street_2=street2,city=city,state=state,
                    country=country,zip_code=zip,job_position=job_position,phone=phone,mobile=mobile,email=email,website=website,tags=tags,individual_image=image).save()
                    print("data is saved")
                    Contact(name=name,title=title,company_name=var,tax_id=tax_id,address_street_1=street1,address_street_2=street2,city=city,state=state,
                    country=country,zip_code=zip,job_position=job_position,phone=phone,mobile=mobile,email=email,website=website,tags=tags,individual_image=image).save()
                    print("contact data is saved")
                except ValueError:
                    render(request,'contact.html',{"error":"Phone and Mobile Number Can't Empty","data1":Company.objects.all()})
        elif user_type == "company":
            print(name,company_name,street1,street2,city,state,zip,country,tax_id,job_position,phone,mobile,email,website,title,tags)
            try:
                Company(title=name,tax_id=tax_id,address_street_1=street1,address_street_2=street2,city=city,state=state,country=country,
                zip_code=zip,phone=phone,mobile=mobile,email=email,website=website,tags=tags,company_image=image).save()
                Contact(cmp_title=name,cmp_tax_id=tax_id,cmp_address_street_1=street1,cmp_address_street_2=street2,cmp_city=city,cmp_state=state,cmp_country=country,
                cmp_zip_code=zip,cmp_phone=phone,cmp_mobile=mobile,cmp_email=email,cmp_website=website,cmp_tags=tags,company_image=image).save()
            except ValueError:
                return render(request, 'contact.html',{"error":"Phone and Mobile Number Can't Empty","data1":Company.objects.all()})   
    return redirect('contact')


def get_comp_details(request):
    value = request.GET["value_1"]
    print("value", value)
    res = Company.objects.get(id=value)
    print("result", res)
    ser = CompanySerializer(res)
    return JsonResponse(ser.data)


def pipeline(request):
    data = Contact.objects.all()
    return render(request,'pipeline.html',{"data":Contact.objects.all()})


def save_pipeline(request):
    contact_id = request.POST.get('contact_id')
    opportunity = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    revenue = request.POST.get('revenue')
    rating = request.POST.get('rating3')
    print(contact_id,opportunity,email,phone,revenue,rating)
    if contact_id == 'Select':
        return render(request,'pipeline.html',{"error":"Please select Organization/Contact","data":Contact.objects.all()})
    else: 
        try:
            c_id = Contact.objects.get(id=contact_id)
            Pipeline(contact=c_id,opportunity=opportunity,email=email,phone=phone,expected_revenue=revenue,rating=rating).save()
        except ValueError:
            return render(request,"pipeline.html",{"error":"Invalid Expected Revenue","data":Contact.objects.all()})
    return redirect('pipeline')


def get_contact_details(request):
    value = request.GET["value_1"]
    print("value", value)
    res = Contact.objects.get(id=value)
    print(res)
    ser = ContactSerializer(res)
    return JsonResponse(ser.data)


def contact_list(request):
    contact = Contact.objects.all()
    context ={
        'data':contact,
    }
    return render(request, 'contact_list.html', context)


def contact_edit(request):
    id = request.GET.get("id")
    contact = Contact.objects.get(id=id)
    print("CONTACT",contact)
    context ={
        'data':contact,
    }
    return render(request, 'contact_edit.html',context)