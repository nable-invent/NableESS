def save_contact(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type',False)
        print(user_type) 
        if user_type == "indivisual":
           #form = IndividualForm(request.POST,request.FILES,None)
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
           print(name, company_name,street1, street2,city,state,zip,country,tax_id,job_position,phone,mobile,email,website,title,tags)
           try:
            Individual(name=name,title=title,tax_id=tax_id,address_street_1=street1,address_street_2=street2,city=city,
            state=state,country=country,zip_code=zip,job_position=job_position,phone=phone,mobile=mobile,email=email,website=website,tags=tags).save()
           except e:
            return render(request, 'contact.html',{"error":e})
           if form.is_valid():
            print("data")
            form.save() 
        elif user_type == "company":
            form = CompanyForm(request.POST,request.FILES)
            if form.is_valid():
                print("data2")
                form.save() 
    return render(request, 'contact.html')

# def company(request):

    # send_to = d_email.split(",")
    # send_to_subject = "Registration OTP"
    # send_to_message = "Your Registration OTP is : " + str(EMAIL_OTP)
    # send_mail(send_to_subject, send_to_message, EMAIL_HOST_USER, send_to,fail_silently=False)

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


# first_name= request.POST.get('first_name')
        # last_name= request.POST.get('last_name')
        # email= request.POST.get('email')
        # phone_number= request.POST.get('phone')
        # password1= request.POST.get('password1')
        # password2= request.POST.get('password2')
        # address= request.POST.get('address')
        # profile_image= request.FILES.get('image')
        # print(first_name,last_name,email,phone_number,password1,password2,address,profile_image)
        # data = CustomUser.objects.create(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,
        # password1=password1,password2=password2,address=address,profile_image=profile_image)
        # data.save()
        # except:
            # return render(request, "signup.html",{"error":"Invalid Data"})