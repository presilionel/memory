from django.urls import path
from .views import mod_index
urlpatterns = [
    path('', mod_index, name='mod-index'),   
]