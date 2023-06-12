from django.http import HttpResponse
from django.shortcuts import render
import folium 
# Create your views here.


def card_index(request):

    m = folium.Map(location=[3.864642047953692, 11.519707959371265], zoom_start = 5)
    folium.Marker([3.864642047953692, 11.519707959371265], tooltip='Click for more', popup='yes').add_to(m)
    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'card/index.html', context)

 