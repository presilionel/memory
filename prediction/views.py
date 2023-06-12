from django.http import HttpResponse
from django.shortcuts import render
from .models import DataCEM
from .forms import DataCEMForm
# Create your views here.


def pred_index(request):
    form = DataCEMForm()
    if request.method == 'POST':
        print(request.POST)
    context = {'form':form}
    return render(request, 'prediction/index.html', context)
