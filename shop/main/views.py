from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .cards import cards
# Create your views here.


#http://127.0.0.1:8000
def home(request):
    #return HttpResponse("Hello World")
    return render(request, 'main/index.html', {'cards':cards})


# параметри url/id   url/title   rozetka.ua/tv
# query params       rozetka.ua?title=tv&start_price=3400&end_price=100000
#

def get_card(request, id):

    if request.GET.get('title'):
        title = request.GET.get('title')
    if id>0 and id<=len(cards):
        return render(request, 'main/card.html', {
            'card':cards[id-1],
            'title':f'{title if title else "Card "+id}'
        })
    else:
        return HttpResponse("Not Found")

def search(request):
    title = request.GET.get('title', '')

    result = [
        card for card in cards
        if title.lower() in card['title'].lower()
    ]

    return render(request, 'main/index.html', {
        'cards': result
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