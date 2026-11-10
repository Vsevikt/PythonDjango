from django.contrib import admin

from main.models import Card, Person

# Register your models here.
admin.site.register(Card)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ("refresh_token",)
