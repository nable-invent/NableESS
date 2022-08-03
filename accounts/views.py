from django.shortcuts import redirect, render
from accounts.models import CustomUser
from django.db import IntegrityError
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER
import random



def otpGenerator():
    otp = random.randint(100000,999999)
    return otp

EMAIL_OTP = ""
EMAIL = ""

def send_mail():
    global EMAIL_OTP,EMAIL
    EMAIL_OTP = otpGenerator()
    print("OTP", EMAIL_OTP)
    # send_to = EMAIL.split(",")
    # send_to_subject = "Registration OTP"
    # send_to_message = "Your Nable CRM Registration OTP is : " + str(EMAIL_OTP)
    # send_mail(send_to_subject, send_to_message, EMAIL_HOST_USER, send_to,fail_silently=False)
    print("Mail Send")


def index(request):
    return render(request,'login.html')


def user_signup(request):
    return render(request,'signup.html',{"form":CustomUserCreationForm()})


def user_register(request):
    if request.method == 'POST':
        cform = CustomUserCreationForm(request.POST,request.FILES)
        print("Data",request.POST.get('email'))
        email = request.POST.get('email')
        if cform.is_valid():
            print("Confirm Data")
            # cform.save(commit = False)

            global EMAIL
            EMAIL = email
            send_mail()
            return render(request,"otp_validation.html")
        else:
            return render(request,'signup.html',{"error":cform.errors,"form":CustomUserCreationForm()})
    else:
        return render(request,'signup.html',{"form":CustomUserCreationForm()}) 


def validate_otp(request):
    otp = int(request.POST.get('otp'))
    if EMAIL_OTP == otp:
        return redirect('index')
    else:
        return render(request,"otp_validation.html",{"error":"Invalid OTP! Please Enter Valid OTP"})


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            uesr = authenticate(request,email=email,password=password)
            if uesr:
                login(request,uesr)
                return redirect('contact_list')
            else:
                return render(request,'login.html',{"error":"Invalid Email or Password !!!"})
        except CustomUser.DoesNotExist:
            return render(request,'login.html',{"error":"Invalid Email or Password !!!"})
    else:
        logout(request)
        return redirect('index')


def resend_otp(request):
    send_mail()
    return render(request,'otp_validation.html',{"error":"OTP Send Again Your Email-Id"})