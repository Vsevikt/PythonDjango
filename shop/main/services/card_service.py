from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.shortcuts import render

from ..cards import cards
from ..models import Card


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


def get_card_by_title(request):
    title = None
    if request.method=='GET' and  request.GET.get('title'):
        title = request.GET.get('title')

    elif request.method=='POST':
        title = request.POST.get('title')
    if title is not None:
        return JsonResponse({'title': title})
    else:
        return HttpResponse("Not Found")


def search(request):
    title = request.GET.get("title", "").strip()
    result = Card.objects.filter(title__icontains=title)

    return render(request, "main/index.html", {
        "cards": result,
    })

def create_card(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        card = Card(
            title=title,
            description=description,
            image=image,
            created_at=timezone.now()
        )
        card.save()

    return JsonResponse({
        'title': title,
        'description': description,
        'image': image.name if image else None
    })