from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import timezone

from ..models import Card

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
    })

def create_card(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed."})

    title = request.POST.get("title", "").strip()
    description = request.POST.get("description", "").strip()
    image = request.FILES.get("image")

    if not title or not description:
        return JsonResponse({"error": "Title and description are required."})

    card = Card.objects.create(
        title=title,
        description=description,
        image=image,
        created_at=timezone.now(),
    )

    return JsonResponse({
        "id": card.id,
        "title": card.title,
        "description": card.description,
        "image_url": card.image.url if card.image else "",
        "detail_url": f"/card/{card.id}",
    })
