from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def pred_index(request):
    if request.method == 'POST':
        filen = request.POST('filen')
        fileqoe = request.POST('fileqoe')
        return HttpResponse('YOUR FILE WAS UPLOADED SUCESSFULLY')
    return render(request, 'prediction/index.html')
