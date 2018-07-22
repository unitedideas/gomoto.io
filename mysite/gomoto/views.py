from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from statistics import *
from datetime import time
from cmath import sqrt
from collections import OrderedDict
import json, importlib, datetime, operator
from django.db.models import Avg, Max, Min, Sum
from .models import Bike


def index(request):
    return render(request, 'gomoto/index.html', {})


def get_bikes(request):
    data_from_vue = json.loads(request.body)
    print(data_from_vue)
    priorities_list = data_from_vue["priorities_list"]
    filters_dict = data_from_vue["filters_dict"]
    # print(filters_list)
    print()
    print(priorities_list)
    print()

    response_dictionary = {}



    bikes = Bike.objects.all()


    # This gives me all bikes
    print(filters_dict)
    bikes = bikes.filter(**filters_dict)
    filters_dict = {}
    print(len(bikes), end=' <--- filtered bike count \n')
    if len(bikes) < 3:
        # return JsonResponse({'bikes':[]}) #<--- Matthew
        return JsonResponse({'message':'There are no motorcycle that meet these filters. GOMOTO some more!', 'bikes':[]})



    bike_score_list = []
    print(bike_score_list)
    print(priorities_list)
    for property in priorities_list:
        property_set = []
        count = 0
        none_count = 0
        print(property)
        for bike in bikes:
            property_value = getattr(bike, property)
            # print(property_value)
            if property_value is None:
                none_count += 1
            elif property_value is not None:
                property_set.append(property_value)
                # print(property_value)

        # mean_list[property]=mean(property_set)
        property_mean = mean(property_set)
        standard_dev = stdev(property_set)

    top_3_bikes = std_dev_calc(property_mean, standard_dev, bikes, priorities_list)

    return_list = []

    keys = []
    for field in Bike._meta.fields:
        if field.name != 'id':
            keys.append(field.name)
    # print (keys)

    for bike in top_3_bikes:
        print(bike)
        values = []
        for field in keys:
            values.append(getattr(bike,field))
        return_list.append(dict(zip(keys, values)))
        # print()
        # print(return_list)
        # print()

    return_data = {'bikes':return_list}
    # print(return_data)

    return JsonResponse(return_data)


def std_dev_calc(property_mean, standard_dev, bikes, priorities_list):
    all_bikes_scores = {}
    count_bikes = 0
    for bike in bikes:
        bike_score = 0
        count = len(priorities_list)
        count_bikes += 1
        for property in priorities_list:
            weighted = count / len(priorities_list)
            # print(weighted)
            bike_prop_value = getattr(bike, property)
            if bike_prop_value is not None:
                z_score = (bike_prop_value - property_mean) / standard_dev * weighted
                if property == 'seatheight' or property == 'weight' or property == 'price':
                    z_score *= -1
                count -= 1
            else:
                z_score = -1
                count -= 1
            bike_score += z_score
        all_bikes_scores[bike] = bike_score

    all_bikes_scores = sorted(all_bikes_scores.items(), key=operator.itemgetter(1), reverse= True)
    all_bikes_scores = dict(all_bikes_scores[:3])
    #
    # for bike in all_bikes_scores:
    #     top_3_bikes.append(bike[0])


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




    # return_data = {'bikes': [
    #     {'year': '2000', 'make': 'Suzuki', 'model': 'dzr 400', 'price': '$9999', 'starter': 'Electric/ Kick',
    #      'dry_weight': '', 'wet_weight': '305 lbs', 'displacement': '399 cc', 'seatheight': '36 in',
    #      'img_src': 'https://www.dirtrider.com/sites/dirtrider.com/files/styles/655_1x_/public/buyers_guide/2018/2018_BETA_RRRaceEdition_480.jpg?itok=aKZE-UeC',
    #      'category': 'Adventure', 'engine_type': 'Four-Stroke', 'weight': '305 lbs'},
    #     {'year': '2015', 'make': 'KTM', 'model': 'ecx 500', 'price': '$12000', 'starter': 'electric',
    #      'dry_weight': '221 lbs', 'wet_weight': '', 'displacement': '505 cc', 'seatheight': '38 in',
    #      'img_src': 'https://dirtbikemagazine.com/wp-content/uploads/2014/11/1141.jpg', 'category': 'Off-Road',
    #      'engine_type': 'Four-Stroke', 'weight': '221 lbs'},
    #     {'year': '1999', 'make': 'Yamaha', 'model': 'XL 250', 'price': '$9000', 'starter': 'Kick', 'dry_weight': '',
    #
    #      'wet_weight': '190 lbs', 'displacement': '445 cc', 'seatheight': '37 in',
    #      'img_src': 'https://dirtbikemagazine.com/wp-content/uploads/2014/11/1141.jpg', 'category': 'MX',
    #      'engine_type': 'Two-Stroke', 'weight': '190 lbs'}]}


    # for bike in top_3_bikes:
    # # for attribute in :
    # #     put each in a dictionary and then all three in a list
    #     print(dir(__bikes__))


    # bikes = Bike.objects.all()
    # print(len(bikes), end=' <------bikes with dry weight')
    # for bike in bikes:
    #     if bike.wet_weight == None:
    #         print()
    #         print(bike.wet_weight, end=' <<---before')
    #         new_weight = bike.dry_weight
    #         bike.wet_weight = new_weight
    #         print()
    #         print(bike.wet_weight, end=' <<---after')
    #         bike.save()