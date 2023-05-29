from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def mod_index(request):
    return render(request, 'modelisation/index.html')