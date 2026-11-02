from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#localhost:127.0.0.1:8000
def home(request):
    # return HttpResponse("Hello World")
    cards = [
        {
            'image': 'main/images/react.png',
            'title': 'React',
            'description': 'JavaScript для створення інтерфейсів',
        },
        {
            'image': 'main/images/aspdotnetcore.png',
            'title': 'Python',
            'description': 'Мова програмування Python',
        },
        {
            'image': 'main/images/django.jpg',
            'title': 'Django',
            'description': 'Фреймворк для розробки веб-застосунків',
        }
    ]
    return render(request, 'main/index.html', {'cards': cards})

def about(request):
    text = 'Це сторінка про Нас. Це точна ця сторінка'
    frameworks = ['flask', 'django', 'fast api']
    return render(request, 'main/about.html', {'text': text, 'frameworks': frameworks})

def services(request):
    return render(request, 'main/services.html')

def contacts(request):
    return render(request, 'main/contacts.html')