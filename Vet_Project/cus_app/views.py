from django.shortcuts import render
from . import views

# Create your views here.
def home(request):
    render(request, 'home.html')

def about(request):
    render(request, 'about.html')

def customers(request):
    render(request, 'customers.html')

def customers_index(request):
    customers = Customer.object.all() 
    return render(request, 'customers/index.html', {'customers': customers})   