from django.shortcuts import render
from .cards import cards
from .models import Card

from .services.card_service import get_card, get_card_by_title, search, create_card
from .services.user_service import registration

# -- card
def get_card_view(request, id):
    return get_card(request, id)

def get_card_by_title_view(request):
    return get_card_by_title(request)

def search_view(request):
    return search(request)

def create_card_view(request):
    return create_card(request)


# -- person
def registration_view(request):
    return registration(request)


def home(request):
    #return HttpResponse("Hello World")
    return render(request, 'main/index.html', {'cards': Card.objects.all()})


def about(request):
    #return HttpResponse("Hello World")
    text = 'Це сторінка про Нас. Це точно ця сторінка'
    frameworks = []
    return render(request, 'main/about.html',
                  {'text': text, 'frameworks': frameworks, 'cards':cards,
                   'data':[1,2,105,102,7,10,100]}  )

def services(request):
    return render(request, 'main/services.html')

def contacts(request):
    return render(request, 'main/contacts.html')