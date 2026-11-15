from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from datetime import datetime, timedelta, timezone
import jwt

from ..models import User

def registration(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        first_name = request.POST.get("first_name").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email").strip()
        date_of_birth = request.POST.get("date_of_birth")
        password = request.POST.get("password")
        password_repeat = request.POST.get("passwordRepeat")
        avatar = request.FILES.get("avatar")

        error = None

        if not first_name or not email or not username:
            error = "Вкажіть ім’я, нікнейм та email."
        elif len(username) > 20:
            error = "Нікнейм має містити не більше 20 символів."
        elif User.objects.filter(username__iexact=username).exists():
            error = "Цей нікнейм уже зайнятий."
        elif len(password) < 8:
            error = "Пароль має містити щонайменше 8 символів."
        elif password != password_repeat:
            error = "Паролі не збігаються."

        if error:
            return render(request, "main/registration.html", {
                "error": error,
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
            })

        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            date_of_birth=date_of_birth,
            password=make_password(password),
            avatar=avatar,
        )
        user.save()

        return set_auth_cookies(redirect("home"), user)

    return render(request, "main/registration.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()

        if user and check_password(password, user.password):
            return set_auth_cookies(redirect("home"), user)

        return render(request, "main/login.html", {
            "error": "Невірне ім’я користувача або пароль."
        })

    return render(request, "main/login.html")


def create_tokens(user):
    now = datetime.now(timezone.utc)

    refresh_token = jwt.encode({
        "user_id": user.pk,
        "type": "refresh",
        "exp": now + timedelta(days=30),
    }, settings.SECRET_KEY, algorithm="HS256")

    user.refresh_token = refresh_token
    user.save(update_fields=["refresh_token"])

    return refresh_token

def set_auth_cookies(response, user):
    refresh_token = create_tokens(user)

    response.set_cookie(
        "refresh_token",
        refresh_token,
        max_age=30*24*60*60,
        httponly=True,
        secure=not settings.DEBUG,
        samesite="Lax",
    )
    return response