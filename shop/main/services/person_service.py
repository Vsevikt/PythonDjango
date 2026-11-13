from datetime import datetime as dt
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import json

from ..models import Person

def registration(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordRepeat = request.POST.get('passwordRepeat')
        avatar = request.FILES.get('avatar')

        if password != passwordRepeat:
            return render(request, 'main/registration.html', {
                'error': 'Паролі не збігаються'
            })

        person = Person(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            avatar=avatar
        )

        person.save()

        return redirect('home')

    return render(request, 'main/registration.html')