from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#localhost:127.0.0.1:8000
def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'main/layout.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def contacts(request):
    return render(request, 'main/contacts.html')