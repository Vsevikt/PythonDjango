from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from ..models import User

def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email").strip()
        date_of_birth = request.POST.get("date_of_birth") or None
        password = request.POST.get("password")
        password_repeat = request.POST.get("passwordRepeat")
        avatar = request.FILES.get("avatar")

        error = None

        if not first_name or not email or not username:
            error = "Вкажіть ім’я та email."
        elif len(password) < 8:
            error = "Пароль має містити щонайменше 8 символів."
        elif password != password_repeat:
            error = "Паролі не збігаються."

        if error:
            return render(request, "main/registration.html", {
                "error": error,
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

        return redirect("home")

    return render(request, "main/registration.html")