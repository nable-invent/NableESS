from django.shortcuts import redirect, render
from accounts.models import CustomUser


def index(request):
    return render(request,'login.html')


def user_signup(request):
    return render(request,'signup.html')


def user_register(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        phone_number= request.POST.get('phone')
        password= request.POST.get('password')
        address= request.POST.get('address')
        profile_image= request.FILES.get('image')
        print(first_name,last_name,email,phone_number,password,address,profile_image)
        # data = CustomUser.objects.create(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,
        # password=password,address=address,profile_image=profile_image)
        # data.save()
        return redirect('index')
