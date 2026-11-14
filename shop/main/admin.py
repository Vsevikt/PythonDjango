from django.contrib import admin

from main.models import Card, User

# Register your models here.
admin.site.register(Card)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("refresh_token",)
