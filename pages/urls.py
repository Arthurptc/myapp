from django.urls import path
from pages.views import about, contact, index, persons

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contact/', contact),
    path('persons/', persons),
]