
from django.urls import path
from .views import pred_index
urlpatterns = [
    path('', pred_index, name='pred-index'),   
]
