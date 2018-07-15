from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from statistics import *
from datetime import time
from cmath import sqrt
from collections import OrderedDict
import json, numpy, importlib, datetime, operator
from django.db.models import Avg, Max, Min, Sum
from .models import Bike


def index(request):
    return render(request, 'gomoto/index.html', {})


def get_bikes(request):
    priorities_dict = json.loads(request.body)
    priorities_list = priorities_dict["priorities_list"]

    # print(priorities_list)
    print('------------------------------------------------------------')
    # todo this will be the top three bikes from the bike_score_list
    response_dictionary = {}
    score_list = [1, 2, 3, 4]
    filter_dict = {}
    bikes = Bike.objects.all()

    # todo implement filter on the VUE (index.html) send back a dictionary
    # This gives me all bikes

    # bikes = bikes.filter(**filter_dict)
    # print('unfiltered count')
    # print(len(bikes))

    # mean_list = {}
    # todo will need to sort the list of dicts - max to min
    bike_score_list = []
    for property in priorities_list:
        print('--------- for all ' + property + " ----------")
        property_set = []
        count = 0
        none_count = 0
        for bike in bikes:
            property_value = getattr(bike, property)
            if property_value is None:
                none_count += 1
            elif property_value is not None:
                property_set.append(property_value)

        # mean_list[property]=mean(property_set)
        property_mean = mean(property_set)
        standard_dev = stdev(property_set)


    print('Finished')

    data = std_dev_calc(property_mean, standard_dev, bikes, priorities_list)

    for bike in data:
        print(bike)


    data = {'bikes': [
        {'year': '2000', 'make': 'Suzuki', 'model': 'dzr 400', 'price': '$9999', 'starter': 'Electric/ Kick',
         'dry_weight': '', 'wet_weight': '305 lbs', 'displacement': '399 cc', 'seatheight': '36 in',
         'img_src': 'https://www.dirtrider.com/sites/dirtrider.com/files/styles/655_1x_/public/buyers_guide/2018/2018_BETA_RRRaceEdition_480.jpg?itok=aKZE-UeC',
         'category': 'Adventure', 'engine_type': 'Four-Stroke', 'weight': '305 lbs'},
        {'year': '2015', 'make': 'KTM', 'model': 'ecx 500', 'price': '$12000', 'starter': 'electric',
         'dry_weight': '221 lbs', 'wet_weight': '', 'displacement': '505 cc', 'seatheight': '38 in',
         'img_src': 'https://dirtbikemagazine.com/wp-content/uploads/2014/11/1141.jpg', 'category': 'Off-Road',
         'engine_type': 'Four-Stroke', 'weight': '221 lbs'},
        {'year': '1999', 'make': 'Yamaha', 'model': 'XL 250', 'price': '$9000', 'starter': 'Kick', 'dry_weight': '',
         'wet_weight': '190 lbs', 'displacement': '445 cc', 'seatheight': '37 in',
         'img_src': 'https://dirtbikemagazine.com/wp-content/uploads/2014/11/1141.jpg', 'category': 'MX',
         'engine_type': 'Two-Stroke', 'weight': '190 lbs'}]}
    return JsonResponse(data)


# todo ### start tallying the points for each bike, getting the top 3 scores
# todo ### supply the top 3 bikes data back to the template (VUE)


def std_dev_calc(property_mean, standard_dev, bikes, priorities_list):
    all_bikes_scores = {}
    count_bikes = 0
    for bike in bikes:
        print('start -------- ' + str(bike) + ' -------')
        bike_score = 0
        count = len(priorities_list)
        count_bikes += 1
        for property in priorities_list:
            weight = count / len(priorities_list)
            bike_prop_value = getattr(bike, property)
            if bike_prop_value is not None:
                z_score = (bike_prop_value - property_mean) / standard_dev * weight
                if property == 'seatheight' or property == 'dry_weight' or property == 'wet_weight':
                    z_score *= -1
                count -= 1
            else:
                z_score = 0
                count -= 1
            bike_score += z_score
        all_bikes_scores[bike] = bike_score

        print(bike_score)
    all_bikes_scores = sorted(all_bikes_scores.items(), key=operator.itemgetter(1), reverse= True)
    all_bikes_scores = all_bikes_scores[:3]
    all_bikes_scores = dict(all_bikes_scores)


    return all_bikes_scores

###---------------------------------------- Testing --------------------------------------###


#
# print(len(bikes))
# count = 0
# for bike in bikes:
#     score = 0
#     # print('------running for '+ str(bike) + ' -------')
#     for property in priorities_list:
#         all_prop_values = []
#         bike
#         prop_value = getattr(bike, property)
#         # std_dev_calc(bikes, priority)
#         count+=1
# print('------------ counts ----------------')
# print(int(count/6))
# print(len(bikes))
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
