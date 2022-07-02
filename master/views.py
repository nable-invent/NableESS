
from django.shortcuts import render
from .forms import CompanyForm
# Create your views here.


def index(request):
    print("AMIT")
    return render(request, 'dashboard.html')

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
    print("AMIT")
    return render(request, 'contact.html')

