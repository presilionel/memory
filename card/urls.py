from django.urls import path
from .views import card_index
urlpatterns = [
    path('', card_index, name='card-index'),   
]