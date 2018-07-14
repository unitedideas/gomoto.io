from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from statistics import stdev
import json, numpy

from .models import Bike


def index(request):
    return render(request, 'gomoto/index.html', {})


def get_bikes(request):
    priorities_list = json.loads(request.body)
    print('------------------------------------------------------------')
    print('get_bikes view')
    print('------------------------------------------------------------')

    print(priorities_list)

    bikes = Bike.objects.filter(price__isnull=False)
    print(len(bikes))

    price_data = []

    for bike in bikes:
        if bike.price is not None:
            price_data.append(int(bike.price))
    price_standard_dev = stdev(price_data)
    print('Price std dev.: ' + str(price_standard_dev))

    response_dictionary = {}

    top_three_bikes = {bikes}

    top_three_bikes = {'bikes':[{'year': '2000','make': 'Suzuki','model': 'dzr 400','price': '$9999','starter': 'Electric/ Kick','dry_weight': '','wet_weight': '305 lbs','displacement': '399 cc','seatheight': '36 in','img_src': 'https://dirtbikemagazine.com/wp-content/uploads/2014/11/1141.jpg','category': 'Adventure','engine_type': 'Four-Stroke','weight': '305 lbs'},{'year': '2015','make': 'KTM','model': 'ecx 500', 'price': '$12000','starter': 'electric', 'dry_weight': '221 lbs','wet_weight': '','displacement': '505 cc','seatheight': '38 in','img_src': 'https://dirtbikemagazine.com/wp-content/uploads/2014/11/1141.jpg','category': 'Off-Road','engine_type': 'Four-Stroke', 'weight': '221 lbs'},{ 'year': '1999',    'make': 'Yamaha',  'model': 'XL 250', 'price': '$9000','starter': 'Kick','dry_weight': '','wet_weight': '190 lbs','displacement': '445 cc','seatheight': '37 in', 'img_src': 'https://dirtbikemagazine.com/wp-content/uploads/2014/11/1141.jpg','category': 'MX','engine_type': 'Two-Stroke','weight': '190 lbs'}]}
    return JsonResponse(top_three_bikes)


# g

def welcome(request):
    print('------------------------------------------------------------')
    print('welcome get_bikes view')
    print('------------------------------------------------------------')
    # run some welcome informational screen here
    welcome = {'welcome':'Welcome to Moto.io. /n Here you can this simple app was created to save you time trying to pick through all the stats of dirt bikes. Look to the right side of the page and drag your top priorities in order starting with the most important at the top. As you do the top three motorcycles that fit your priorities will adjust on the screen. That\'s it!!!. Have fun. \n -Shane'}
    return render(request, 'gomoto/index.html', {})
