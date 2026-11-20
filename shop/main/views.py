from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from .cards import cards
from .models import Card, Tag
from .forms import FormCreateCard

from .services.card_service import get_card, get_card_by_title, search, create_card as create_card_api
from .services.user_service import registration, login

# -- card
def get_card_view(request, id):
    return get_card(request, id)

def get_card_by_title_view(request):
    return get_card_by_title(request)

def search_view(request):
    return search(request)

def create_card_view(request):
    return create_card_api(request)

# --- for page card_form.html

def create_card_page(request):
    if request.method == 'POST':
        form = FormCreateCard(request.POST, request.FILES)
        if form.is_valid():
            card = Card.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data.get('image') or '',
                created_at=timezone.now(),
            )
            card.tags.set(form.cleaned_data['tags'])
            return redirect('home')
    else:
        form = FormCreateCard()

    return render(request, 'main/card_form.html', {'form': form})


def create_card(request):
    return create_card_page(request)

# ---

# -- person
def registration_view(request):
    return registration(request)

def login_view(request):
    return login(request)

def home(request):
    #return HttpResponse("Hello World")
    return render(request, 'main/index.html', {
        'cards': Card.objects.all(),
        'tags': Tag.objects.all(),
        'form': FormCreateCard(),
    })

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

