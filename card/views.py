from django.http import HttpResponse
from django.shortcuts import render
import folium 
# Create your views here.


def card_index(request):

    m = folium.Map(location=[9.6635556,4.075445457598786], zoom_start = 4)
    folium.Marker([19,-12], tooltip='Click for more', popup='yes').add_to(m)
    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'card/index.html', context)

 