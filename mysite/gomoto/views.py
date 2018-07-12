from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from statistics import stdev
import json, numpy

from .models import Bike

def index(request):
    return render(request, 'gomoto/index.html', {})


def get_bikes(request):
    priorities_list = json.loads(request.body)
    print('Hi There')
    print(priorities_list)

    bikes = Bike.objects.filter(price__isnull = False)
    print(bikes)
    price_data =[]
    for bike in bikes:
        if bike.price is not None:
            price_data.append(int(bike.price))
    price_standard_dev = stdev(price_data)
    print(price_standard_dev)

    return render(request, 'gomoto/index.html', {})

