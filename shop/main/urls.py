from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('card/<int:id>', views.get_card, name='card'),
    path('search/', views.search, name='search'),
    path('create', views.create_card, name='create'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
    path('registration', views.registration, name='registration'),
]