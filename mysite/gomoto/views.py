from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from statistics import *
from cmath import sqrt
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

    response_dictionary = {}

    # standard_dev
    #
    # 1. Work out the Mean
    # 2. for each number: subtract the Mean and square the result
    # 3. mean of those squared differences
    # 4. Take the square root of that

    price_standard_dev = 0
    data = []

    bikes = bikes.filter(engine_type = 'Two-stroke')
    bikes = bikes.filter(category = 'Off-Road')

    for bike in bikes:
        if bike.price is not None:
            data.append(int(bike.price))
    std_dev_calc(data, 'price')

    data = []
    bikes = Bike.objects.filter(seatheight__isnull=False)
    bikes = bikes.filter(engine_type = 'Two-stroke')
    bikes = bikes.filter(category = 'Off-Road')

    for bike in bikes:
        if bike.seatheight is not None:
            data.append(int(bike.seatheight))
    std_dev_calc(data, 'seatheight')

    data = []
    bikes = Bike.objects.filter(dry_weight__isnull=False)
    bikes = bikes.filter(engine_type = 'Two-stroke')
    bikes = bikes.filter(category = 'Off-Road')

    for bike in bikes:
        if bike.dry_weight is not None:
            data.append(int(bike.dry_weight))
    std_dev_calc(data, 'dry_weight')

    data = []
    bikes = Bike.objects.filter(wet_weight__isnull=False)
    bikes = bikes.filter(engine_type = 'Two-stroke')
    bikes = bikes.filter(category = 'Off-Road')

    for bike in bikes:
        if bike.wet_weight is not None:
            data.append(int(bike.wet_weight))
    std_dev_calc(data, 'wet_weight')

    data = []
    bikes = Bike.objects.filter(displacement__isnull=False)

    bikes = bikes.filter(engine_type = 'Two-stroke')
    bikes = bikes.filter(category = 'Off-Road')

    print('filter two-stroke '+str(len(bikes)))
    for bike in bikes:
        if bike.displacement is not None:
            data.append(int(bike.displacement))
    std_dev_calc(data, 'displacement')







    # top_three_bikes = {bikes}

    top_three_bikes = {'bikes':[{'year': '2000','make': 'Suzuki','model': 'dzr 400','price': '$9999','starter': 'Electric/ Kick','dry_weight': '','wet_weight': '305 lbs','displacement': '399 cc','seatheight': '36 in','img_src': 'https://dirtbikemagazine.com/wp-content/uploads/2014/11/1141.jpg','category': 'Adventure','engine_type': 'Four-Stroke','weight': '305 lbs'},{'year': '2015','make': 'KTM','model': 'ecx 500', 'price': '$12000','starter': 'electric', 'dry_weight': '221 lbs','wet_weight': '','displacement': '505 cc','seatheight': '38 in','img_src': 'https://dirtbikemagazine.com/wp-content/uploads/2014/11/1141.jpg','category': 'Off-Road','engine_type': 'Four-Stroke', 'weight': '221 lbs'},{ 'year': '1999',    'make': 'Yamaha',  'model': 'XL 250', 'price': '$9000','starter': 'Kick','dry_weight': '','wet_weight': '190 lbs','displacement': '445 cc','seatheight': '37 in', 'img_src': 'https://dirtbikemagazine.com/wp-content/uploads/2014/11/1141.jpg','category': 'MX','engine_type': 'Two-Stroke','weight': '190 lbs'}]}
    return JsonResponse(top_three_bikes)




def welcome(request):
    print('------------------------------------------------------------')
    print('welcome get_bikes view')
    print('------------------------------------------------------------')
    # run some welcome informational screen here
    welcome = {'welcome':'Welcome to Moto.io. /n Here you can this simple app was created to save you time trying to pick through all the stats of dirt bikes. Look to the right side of the page and drag your top priorities in order starting with the most important at the top. As you do the top three motorcycles that fit your priorities will adjust on the screen. That\'s it!!!. Have fun. \n -Shane'}
    return render(request, 'gomoto/index.html', {})


def std_dev_calc(set, name):
    number_standard_dev = numpy.std(set, axis = 0)
    number_standard_dev = round(number_standard_dev,2)

    mean_number = 0
    mean_number = mean(set)

    number_minus_mean_list = []

    number_minus_mean = 0

    for number in set:
        number_minus_mean = number - mean_number
        number_minus_mean_list.append(number_minus_mean)
    sqrd_diff_mean = (sum(number_minus_mean_list))/ (len(number_minus_mean_list)-1)

    sqrroot = sqrt(sqrd_diff_mean)

    sqrroot = str(sqrroot)
    sqrroot = sqrroot[:5]

    numpystd = numpy.std(set)

    print("")
    print('-------------start ' + name + ' -----------')
    print('calculated steps ' + sqrroot)
    print('numpy.std ' + str(numpystd))
    print('std dev.: ' + str(number_standard_dev))
    print('-------------end ' + name + ' ------------')
    print("")








