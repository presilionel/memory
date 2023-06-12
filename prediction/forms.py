from django.forms import ModelForm
from .models import DataCEM

class DataCEMForm(ModelForm):
    class Meta:
        model = DataCEM
        fields = '__all__'
        