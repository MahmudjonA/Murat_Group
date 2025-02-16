from django.contrib import admin
from .models import MainPage,Employees


@admin.register(MainPage)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id' , 'company_img' , 'aboutCompany','history','founder','founded_year','location'] 
@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['id' , 'photo' , 'first_name','last_name','position']