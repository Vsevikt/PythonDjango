from django.contrib import admin

from main.models import Card, User, Tag

# Register your models here.
admin.site.register(Card)
admin.site.register(Tag)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("refresh_token",)
