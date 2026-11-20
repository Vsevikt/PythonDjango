from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
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
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed."})

    form = FormCreateCard(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({"errors": form.errors}, status=400)

    card = form.save(commit=False)
    card.created_at = timezone.now()
    card.save()
    form.save_m2m()

    return JsonResponse({
        "id": card.id,
        "title": card.title,
        "description": card.description,
        "image_url": card.image.url if card.image else "",
        "detail_url": f"/card/{card.id}",
    })
