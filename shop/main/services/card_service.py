from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from ..models import Card, Tag
from ..forms import FormCreateCard

def get_card(request, id):
    card = Card.objects.filter(pk=id).first()

    if card is None:
        return HttpResponse("Not Found")

    return render(request, "main/card.html", {
        "card": card,
        "title": card.title,
    })

def get_card_by_title(request):
    if request.method == "GET":
        title = request.GET.get("title", "").strip()
    elif request.method == "POST":
        title = request.POST.get("title", "").strip()
    else:
        return HttpResponse("Method Not Allowed")

    if not title:
        return HttpResponse("Not Found")

    return JsonResponse({"title": title})

def search(request):
    title = request.GET.get("title", "").strip()
    cards = Card.objects.filter(title__icontains=title)

    return render(request, "main/index.html", {
        "cards": cards,
        "search_title": title,
        "tags": Tag.objects.all(),
        "form": FormCreateCard(),
    })

def create_card(request):
    if request.method == "POST":
        print('Отриман POST-request!')
        print('Дані:', request.POST)
        print('Кукі:', request.COOKIES)

    form = FormCreateCard(request.POST, request.FILES)

    if not form.is_valid():
        return render(request, "main/index.html", {
            "cards": Card.objects.all(),
            "tags": Tag.objects.all(),
            "form": form,
        })

    card = Card.objects.create(
        title=form.cleaned_data['title'],
        description=form.cleaned_data['description'],
        image=form.cleaned_data['image'],
        created_at=timezone.now(),
    )

    card.tags.set(form.cleaned_data['tags'])

    return redirect("/search")