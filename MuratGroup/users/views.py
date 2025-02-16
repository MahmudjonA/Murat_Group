from django.shortcuts import render
from .models import MainPage, Employees

def main(request):
    about = MainPage.objects.all().order_by('-id')
    context = {
        "about": about
    }
    return render(
        request=request,
        template_name='index.html',
        context=context,
    )

def employees(request):
    persons = Employees.objects.all().order_by('-id')
    context = {
        "employees": persons 
    }
    return render(
        request=request,
        template_name='employees.html',
        context=context,
    )

def contact(request):
    return render(request, 'contact.html')
