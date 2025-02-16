from django.urls import path
from .views import main, employees, contact

urlpatterns = [
    path('', main, name='main'),
    path('employees/', employees, name='employees'),
     path('contact/', contact, name='contact'),
]
