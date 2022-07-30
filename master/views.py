
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
from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER
# Create your views here.


def contact(request):
    return render(request,'contact.html',{"data1":Company.objects.all()})


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
        phone = request.POST.get('phone') 
        mobile = request.POST.get('mobile') 
        email = request.POST.get('email') 
        website = request.POST.get('website') 
        title = request.POST.get('title') 
        tags = request.POST.get('tags') 
        image = request.FILES.get('image')
        notes = request.POST.get('notes')
        sales = request.POST.get('sales')
        reference = request.POST.get('reference')
        industry = request.POST.get('industry')
        user_type = request.POST.get('user_type',False)
        print(user_type)
        if user_type == "indivisual":
            if company_name == 'Select Company':
                return render(request,'contact.html',{"error":"Please Select Company Name","data1":Company.objects.all()})
            else:
                if image != None:
                    var = Company.objects.get(id=company_name)
                    #form = IndividualForm(request.POST,request.FILES,None)
                    print(name,company_name,street1,street2,city,state,zip,country,tax_id,job_position,phone,mobile,email,website,title,tags,image,notes,sales,reference)
                    try:
                        idata = Individual.objects.create(name=name,title=title,company_name=var,tax_id=tax_id,address_street_1=street1,address_street_2=street2,city=city,state=state,
                        country=country,zip_code=zip,job_position=job_position,phone=phone,mobile=mobile,email=email,website=website,tags=tags,image=image,internal_notes=notes,sales_person=sales,refrence=reference)
                        idata.save()
                        print("data is saved")
                        id = Individual.objects.get(id=idata.id)
                        cdata = Contact.objects.create(name=name,title=title,company_name=var,individual=id,tax_id=tax_id,address_street_1=street1,address_street_2=street2,city=city,state=state,
                        country=country,zip_code=zip,job_position=job_position,phone=phone,mobile=mobile,email=email,website=website,tags=tags,individual_image=image,internal_notes=notes,sales_person=sales,refrence=reference)
                        cdata.save()
                        print("contact data is saved")
                    except ValueError:
                        render(request,'contact.html',{"error":"Phone and Mobile Number Can't Empty","data1":Company.objects.all()})
                else:
                    var = Company.objects.get(id=company_name)
                    #form = IndividualForm(request.POST,request.FILES,None)
                    print(name,company_name,street1,street2,city,state,zip,country,tax_id,job_position,phone,mobile,email,website,title,tags,image,notes,sales,reference)
                    try:
                        idata = Individual.objects.create(name=name,title=title,company_name=var,tax_id=tax_id,address_street_1=street1,address_street_2=street2,city=city,state=state,
                        country=country,zip_code=zip,job_position=job_position,phone=phone,mobile=mobile,email=email,website=website,tags=tags,internal_notes=notes,sales_person=sales,refrence=reference)
                        idata.save()
                        print("data is saved")
                        id = Individual.objects.get(id=idata.id)
                        cdata = Contact.objects.create(name=name,title=title,company_name=var,individual=id,tax_id=tax_id,address_street_1=street1,address_street_2=street2,city=city,state=state,
                        country=country,zip_code=zip,job_position=job_position,phone=phone,mobile=mobile,email=email,website=website,tags=tags,company_image=image,internal_notes=notes,sales_person=sales,refrence=reference)
                        cdata.save()
                        print("contact data is saved")
                    except ValueError:
                        render(request,'contact.html',{"error":"Phone and Mobile Number Can't Empty","data1":Company.objects.all()})
        elif user_type == "company":
            print(name,street1,street2,city,state,zip,country,tax_id,job_position,phone,mobile,email,website,tags,image,notes,sales,reference,industry)
            if image != None:
                print("Image")
                try:
                    cdata = Company.objects.create(name=name,tax_id=tax_id,address_street_1=street1,address_street_2=street2,city=city,state=state,country=country,
                    zip_code=zip,phone=phone,mobile=mobile,email=email,website=website,tags=tags,image=image,internal_notes=notes,sales_person=sales,refrence=reference,industry=industry)
                    cdata.save()

                    cid = Company.objects.get(id=cdata.id)
                    Contact(cmp_title=name,company=cid,cmp_tax_id=tax_id,cmp_address_street_1=street1,cmp_address_street_2=street2,cmp_city=city,cmp_state=state,cmp_country=country,
                    cmp_zip_code=zip,cmp_phone=phone,cmp_mobile=mobile,cmp_email=email,cmp_website=website,cmp_tags=tags,company_image=image,cmp_internal_notes=notes,cmp_sales_person=sales,cmp_refrence=reference,cmp_industry=industry).save()
                except ValueError:
                    return render(request, 'contact.html',{"error":"Phone and Mobile Number Can't Empty","data1":Company.objects.all()})
            else:
                print("image12223")
                try:
                    cdata = Company.objects.create(name=name,tax_id=tax_id,address_street_1=street1,address_street_2=street2,city=city,state=state,country=country,
                    zip_code=zip,phone=phone,mobile=mobile,email=email,website=website,tags=tags,internal_notes=notes,sales_person=sales,refrence=reference,industry=industry)
                    cdata.save()

                    cid = Company.objects.get(id=cdata.id)
                    Contact(cmp_title=name,company=cid,cmp_tax_id=tax_id,cmp_address_street_1=street1,cmp_address_street_2=street2,cmp_city=city,cmp_state=state,cmp_country=country,
                    cmp_zip_code=zip,cmp_phone=phone,cmp_mobile=mobile,cmp_email=email,cmp_website=website,cmp_tags=tags,individual_image=image,cmp_internal_notes=notes,cmp_sales_person=sales,cmp_refrence=reference,cmp_industry=industry).save()
                except ValueError:
                    return render(request, 'contact.html',{"error":"Phone and Mobile Number Can't Empty","data1":Company.objects.all()})   
    return redirect('contact_list')


def get_comp_details(request):
    value = request.GET["value_1"]
    print("value", value)
    res = Company.objects.get(id=value)
    print("result", res)
    ser = CompanySerializer(res)
    return JsonResponse(ser.data)


def pipeline_add(request):
    return render(request,'pipeline_add.html',{"data":Contact.objects.all()})


def save_pipeline(request):
    contact_id = request.POST.get('contact_id')
    opportunity = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    revenue = request.POST.get('revenue')
    rating = request.POST.get('rating3')
    print(contact_id,opportunity,email,phone,revenue,rating)
    if contact_id == 'Select':
        return render(request,'pipeline_add.html',{"error":"Please select Organization/Contact","data":Contact.objects.all()})
    else: 
        try:
            c_id = Contact.objects.get(id=contact_id)
            Pipeline(contact=c_id,opportunity=opportunity,email=email,phone=phone,expected_revenue=revenue,rating=rating).save()
        except ValueError:
            return render(request,"pipeline_add.html",{"error":"Invalid Expected Revenue","data":Contact.objects.all()})
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
    print("Contact",contact)
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
        'data1': Company.objects.all(),
        "var":'none'
    }
    return render(request, 'contact_edit.html',context)


def update_contact(request):
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
        phone = request.POST.get('phone') 
        mobile = request.POST.get('mobile') 
        email = request.POST.get('email') 
        website = request.POST.get('website') 
        title = request.POST.get('title') 
        tags = request.POST.get('tags') 
        image = request.FILES.get('image')
        notes = request.POST.get('notes')
        sales = request.POST.get('sales')
        reference = request.POST.get('reference')
        industry = request.POST.get('industry')
        user_type = request.POST.get('user_type',False)
        c_id = request.GET.get('id')
        print("IDS",c_id)
        print(user_type)
        var = Contact.objects.get(id=c_id)
        print(name,company_name,street1,street2,city,state,zip,country,tax_id,job_position,phone,mobile,email,website,title,tags,image,notes,sales,reference)
        if user_type == "indivisual":
            if company_name == 'Select Company':
                return render(request,'contact_edit.html',{"error":"Please Select Company Name","data1":Company.objects.all()})
            else:
                var2 = var.individual.id
                print("Indivisual", var2)
                cid = Company.objects.get(id=company_name)
                try:
                    data = Individual.objects.get(id=var2)
                    print("data",data)
                    data.name=name
                    data.title=title
                    data.company_name=cid
                    data.tax_id=tax_id
                    data.address_street_1=street1
                    data.address_street_2=street2
                    data.city=city
                    data.state=state
                    data.country=country
                    data.zip_code=zip
                    data.job_position=job_position
                    data.mobile=mobile
                    data.email=email
                    data.website=website
                    data.tags=tags
                    data.image=image
                    data.internal_notes=notes
                    data.sales_person=sales
                    data.refrence=reference
                    data.save()
                    print("data is saved")
                    cdata = Contact.objects.get(id = c_id)
                    print("Contact", cdata) 
                    cdata.name=name
                    cdata.title=title
                    cdata.company_name=cid
                    cdata.individual=data
                    cdata.tax_id=tax_id
                    cdata.address_street_1=street1
                    cdata.address_street_2=street2
                    cdata.city=city
                    cdata.state=state
                    cdata.country=country
                    cdata.zip_code=zip
                    cdata.job_position=job_position
                    cdata.phone=phone
                    cdata.mobile=mobile
                    cdata.email=email
                    cdata.website=website
                    cdata.tags=tags
                    cdata.image=image
                    cdata.internal_notes=notes
                    cdata.sales_person=sales
                    cdata.refrence=reference
                    cdata.save()
                    print("contact data is saved")
                except ValueError:
                    render(request,'contact_edit.html',{"error":"Phone and Mobile Number Can't Empty","data1":Company.objects.all()})
        elif user_type == "company":
            com_id = var.company.id
            comp = Company.objects.get(id=com_id)
            print("Company", comp)
            print(name,street1,street2,city,state,zip,country,tax_id,job_position,phone,mobile,email,website,tags,image,notes,sales,reference,industry)
            try:
                comp.name=name
                comp.tax_id=tax_id
                comp.address_street_1=street1
                comp.address_street_2=street2
                comp.city=city
                comp.state=state
                comp.country=country
                comp.zip_code=zip
                comp.phone=phone
                comp.mobile=mobile
                comp.email=email
                comp.website=website
                comp.tags=tags
                comp.image=image
                comp.internal_notes=notes
                comp.sales_person=sales
                comp.refrence=reference
                comp.industry=industry
                comp.save()
                print("Company data is saved")
                con = Contact.objects.get(id=c_id)
                con.cmp_title=name
                con.cmp_tax_id=tax_id
                con.company=comp
                con.cmp_address_street_1=street1
                con.cmp_address_street_2=street2
                con.cmp_city=city
                con.cmp_state=state
                con.cmp_country=country
                con.cmp_zip_code=zip
                con.cmp_phone=phone
                con.cmp_mobile=mobile
                con.cmp_email=email
                con.cmp_website=website
                con.cmp_tags=tags
                con.company_image=image
                con.cmp_internal_notes=notes
                con.cmp_sales_person=sales
                con.cmp_refrence=reference
                con.cmp_industry=industry
                con.save()
                print("Contact data is saved")
            except ValueError:
                return render(request, 'contact_edit.html',{"error":"Phone and Mobile Number Can't Empty","data1":Company.objects.all()})            
    return redirect('contact_list')    


def delete_contact(request):
    id = request.GET.get('id')
    data = Contact.objects.get(id=id)
    cdata = data.cmp_title
    if cdata:
        print("Company")
        cid = data.company.id
        Company.objects.filter(id=cid).delete()
        print("Company Delete")
        Contact.objects.filter(id=id).delete()
        print("Contact Delete")
    else:
        print("Indivisual")
        iid = data.individual.id
        Individual.objects.filter(id=iid).delete()
        print("Individual Delete")
        Contact.objects.filter(id=id).delete()
        print("Contact Delete")
    return redirect('contact_list')


def pipeline(request):
    pipeline = Pipeline.objects.all()
    context = {
        'data':pipeline,
    }
    return render(request, 'pipeline.html', context)


def pipeline_edit(request):
    id = request.GET.get("id")
    pipeline = Pipeline.objects.get(id=id)
    print("Pipeline",pipeline)
    context ={
        'data':Contact.objects.all(),
        'data1': pipeline,
    }
    return render(request, 'pipeline_edit.html',context)


def update_pipeline(request):
    contact_id = request.POST.get('contact_id')
    opportunity = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    revenue = request.POST.get('revenue')
    rating = request.POST.get('rating3')
    pid = request.GET.get('id')
    pdata = Pipeline.objects.get(id=pid)
    print(contact_id,opportunity,email,phone,revenue,rating)
    if contact_id == 'Select':
        return render(request,'pipeline_edit.html',{"error":"Please select Organization/Contact","data":Contact.objects.all()})
    else: 
        try:
            c_id = Contact.objects.get(id=contact_id)
            pdata.contact=c_id
            pdata.opportunity=opportunity
            pdata.email=email
            pdata.phone=phone
            pdata.expected_revenue=revenue
            pdata.rating=rating
            pdata.save()
        except ValueError:
            return render(request,"pipeline_edit.html",{"error":"Invalid Expected Revenue","data":Contact.objects.all()})
    return redirect('pipeline')


def delete_pipeline(request):
    id = request.GET.get('id')
    print("ID",id)
    Pipeline.objects.filter(id=id).delete()
    return redirect('pipeline')


def change_pipeline_status(request):
    id = request.GET["value_1"]
    status = request.GET["status"]
    print("value", id, status)
    res = Pipeline.objects.get(id=id)
    print(res)
    res.status = status
    res.save()
    # ser = ContactSerializer(res)
    messase = {"data":"Status Change Successfully"}
    return JsonResponse(messase)