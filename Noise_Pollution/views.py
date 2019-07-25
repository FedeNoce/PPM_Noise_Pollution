from django.shortcuts import render
from django.http import HttpResponse
from.models import Sensore, Dati
from django.template import loader


# Create your views here.
def index(request):
    sensori_list = Sensore.objects.order_by('id')[:5]
    template = loader.get_template('Noise_Pollution/index.html')
    context = {
        'sensori_list': sensori_list,
    }
    return render(request, 'Noise_Pollution/index.html', context)


def graphic(request, id):
    dati_list = []
    for object in Dati.objects.all():
        if object.sensore.id == id:
            dati_list.append(object)
    template = loader.get_template('Noise_Pollution/graphic.html')
    return render(request, 'Noise_Pollution/graphic.html', {'dati_list': dati_list})
