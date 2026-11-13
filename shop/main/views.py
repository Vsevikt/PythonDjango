from datetime import datetime as dt

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import json

from . import models
from .cards import cards
from .services.card_service import get_card, get_card_by_title, search, create_card

def get_card_view(request, id):
    return get_card(request, id)

def get_card_by_title_view(request):
    return get_card_by_title(request)

def search_view(request):
    return search(request)

def create_card_view(request):
    return create_card(request)


from .services.person_service import registration

def registration_view(request):
    return registration(request)


# Create your views here.

#http://127.0.0.1:8000
def home(request):
    #return HttpResponse("Hello World")
    return render(request, 'main/index.html', {'cards':cards})


# параметри url/id   url/title   rozetka.ua/tv
# query params       rozetka.ua?title=tv&start_price=3400&end_price=100000
#

# -- card
def get_card_view(request, id):
    return get_card(request, id)

def get_card_by_title_view(request):
    return get_card_by_title_view(request)


def search_view(request):
    return search(request)


def create_card_view(request):
    return create_card(request)




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