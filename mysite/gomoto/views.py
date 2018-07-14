from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from statistics import *
from cmath import sqrt
import json, numpy, importlib
from django.db.models import Avg, Max, Min, Sum
from .models import Bike


def index(request):
    return render(request, 'gomoto/index.html', {})


def get_bikes(request):
    priorities_dict = json.loads(request.body)
    priorities_list = priorities_dict["priorities_list"]

    print(priorities_list)
    print('------------------------------------------------------------')
    print('get_bikes view')
    print('------------------------------------------------------------')
    print(priorities_dict)
    response_dictionary = {}
    score_list = [1,2,3,4]
    bikes = Bike.objects.all()
    print(len(bikes))
    count = 0
    for bike in bikes:
        score = 0
        print('------running for '+ str(bike) + ' -------')
        for property in priorities_list:

            print(getattr(bike, property))
            count+=1
    print('------------ counts ----------------')
    print(count/5)
    print(len(bikes))
    # for priority in priorities_dict:
    #     values_list = Bike.objects.values_list()
    #     for value in values_list:
    #        pass
            # std_dev_calc(bikes,priority)



    # bike = ''
    # bikes = Bike.objects.all()
    # bikes = bikes.filter(displacement__gte=10)
    # bikes = bikes.filter(category = 'Trials')
    # print(bikes)
    #
    #
    # price_standard_dev = 0
    # data = []
    #
    # bikes = Bike.objects.filter(price__isnull=False)
    # bikes = bikes.filter(engine_type = 'Four-stroke')
    # bikes = bikes.filter(category = 'Off-Road')
    # bikes = bikes.filter(displacement__gte=551)
    #
    # for bike in bikes:
    #     if bike.price is not None:
    #         data.append(int(bike.price))
    # std_dev_calc(data, 'price')



    # top_three_bikes = {bikes}

    top_three_bikes = {'bikes':[{'year': '2000','make': 'Suzuki','model': 'dzr 400','price': '$9999','starter': 'Electric/ Kick','dry_weight': '','wet_weight': '305 lbs','displacement': '399 cc','seatheight': '36 in','img_src': 'https://dirtbikemagazine.com/wp-content/uploads/2014/11/1141.jpg','category': 'Adventure','engine_type': 'Four-Stroke','weight': '305 lbs'},{'year': '2015','make': 'KTM','model': 'ecx 500', 'price': '$12000','starter': 'electric', 'dry_weight': '221 lbs','wet_weight': '','displacement': '505 cc','seatheight': '38 in','img_src': 'https://dirtbikemagazine.com/wp-content/uploads/2014/11/1141.jpg','category': 'Off-Road','engine_type': 'Four-Stroke', 'weight': '221 lbs'},{ 'year': '1999',    'make': 'Yamaha',  'model': 'XL 250', 'price': '$9000','starter': 'Kick','dry_weight': '','wet_weight': '190 lbs','displacement': '445 cc','seatheight': '37 in', 'img_src': 'https://dirtbikemagazine.com/wp-content/uploads/2014/11/1141.jpg','category': 'MX','engine_type': 'Two-Stroke','weight': '190 lbs'}]}
    return JsonResponse(top_three_bikes)




# todo ### start tallying the points for each bike, getting the top 3 scores
# todo ### supply the top 3 bikes data back to the template (VUE)


def std_dev_calc(set, name):
    scores = []
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
    print(scores)
    print()
    print('-------------stop ' + name + ' bike '+ str(count) + ' -----------')





