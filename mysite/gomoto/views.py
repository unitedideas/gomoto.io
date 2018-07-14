from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from statistics import *
from cmath import sqrt
import json, numpy
from django.db.models import Avg, Max, Min, Sum
from .models import Bike


def index(request):
    return render(request, 'gomoto/index.html', {})


def get_bikes(request):
    priorities_list = json.loads(request.body)
    print('------------------------------------------------------------')
    print('get_bikes view')
    print('------------------------------------------------------------')

    print(priorities_list)

    bikes = Bike.objects.filter(category = 'Adventure')



    for bike in bikes:
        print(bike.engine_type)


    response_dictionary = {}
    bike = ''
    bikes = Bike.objects.all()
    bikes = bikes.filter(displacement__gte=10)
    bikes = bikes.filter(category = 'Trials')
    print(bikes)


    price_standard_dev = 0
    data = []

    bikes = Bike.objects.filter(price__isnull=False)
    bikes = bikes.filter(engine_type = 'Four-stroke')
    bikes = bikes.filter(category = 'Off-Road')
    bikes = bikes.filter(displacement__gte=551)

    for bike in bikes:
        if bike.price is not None:
            data.append(int(bike.price))
    std_dev_calc(data, 'price')

    data = []
    bikes = Bike.objects.filter(seatheight__isnull=False)
    bikes = bikes.filter(engine_type = 'Four-stroke')
    bikes = bikes.filter(category = 'Off-Road')
    bikes = bikes.filter(displacement__gte=551)

    for bike in bikes:
        if bike.seatheight is not None:
            data.append(int(bike.seatheight))
    std_dev_calc(data, 'seatheight')

    data = []
    bikes = Bike.objects.filter(dry_weight__isnull=False)
    bikes = bikes.filter(engine_type = 'Four-stroke')
    bikes = bikes.filter(category = 'Off-Road')
    bikes = bikes.filter(displacement__gte=551)

    for bike in bikes:
        if bike.dry_weight is not None:
            data.append(int(bike.dry_weight))
    std_dev_calc(data, 'dry_weight')

    data = []
    bikes = Bike.objects.filter(wet_weight__isnull=False)
    bikes = bikes.filter(engine_type = 'Four-stroke')
    bikes = bikes.filter(category = 'Off-Road')
    bikes = bikes.filter(displacement__gte=551)

    for bike in bikes:
        if bike.wet_weight is not None:
            data.append(int(bike.wet_weight))
    std_dev_calc(data, 'wet_weight')

    data = []
    bikes = Bike.objects.filter(displacement__isnull=False)
    bikes = bikes.filter(engine_type = 'Four-stroke')
    print(len(bikes))
    bikes = bikes.filter(category = 'Off-Road')
    print(len(bikes))
    bikes = bikes.filter(displacement__gte=551)
    print(len(bikes))


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
    standard_dev = stdev(set)
    count = 0
    over_2_count = 0
    print()
    print()
    print('-------------start ' + name + ' bike '+ str(count) + ' -----------')
    for num in set:
        std_dev_from_mean = (num - mean(set)) / standard_dev
        count += 1
        if std_dev_from_mean > 1 or std_dev_from_mean < -1:
            over_2_count += 1
            print()
            print(num)
            print(mean(set))
            print(std_dev_from_mean)
            print(standard_dev)
            print()

        #
        #
        # print()
        # print('object 1')
        # print(set[0])
        # print()
        # print('mean')
    print()
    print('Count of over 2 std devs')
    print(over_2_count)
    print()
        # print(mean(set))
        # print()
        # print('std dev.: ' + str(standard_dev))
        # print()
        # print('std dev\'s from mean')
        # print(std_dev_from_mean)
        # print()
    print('-------------stop ' + name + ' bike '+ str(count) + ' -----------')
        # print()
        # print()
        # print()




