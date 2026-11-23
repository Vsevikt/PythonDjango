from datetime import datetime

from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from .cards import cards
from .models import Card, Tag
from .forms import FormCreateCard

from .services.card_service import get_card, get_card_by_title, search, create_card
from .services.user_service import registration, login

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

def login_view(request):
    return login(request)

def home(request: HttpRequest) -> HttpResponse:
    login = request.COOKIES.get('login')

    visits = request.COOKIES.get('visits')

    if visits is None:
        visit_message = 'Вітаємо! Це ваш перший візит.'
        visits = 1
    else:
        visits = int(visits)
        visit_message = f'Ви вже відвідували сайт {visits} разів.'
        visits += 1

    response = render(request, 'main/index.html', {
        'cards': Card.objects.all(),
        'login': login,
        'user': login,
        'tags': Tag.objects.all(),
        'form': FormCreateCard(),
        'visit_message': visit_message,
    })

    response.set_cookie('visits', visits, max_age=3600, httponly=True)

    if login is None:
        response.set_cookie('login', 'admin', httponly=True, max_age=3600)


    return response




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

def test_create(request):
    card = Card(
        title='test card',
        description='test description',
        image='test image',
        create_at=datetime.now(),
    )
    card.save()
    tag = Tag.objects.create(
        name='test_tag',
    )
    card.tags.add(tag)

    return HttpResponse("ok")

