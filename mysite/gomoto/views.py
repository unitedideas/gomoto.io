from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import json
from .models import Bike

def index(request):
    return render(request, 'gomoto/index.html', {})


def get_bikes(request):

    todo_items = TodoAjaxItem.objects.all()
    data = {'todo_items': []}
    for todo_item in todo_items:
        data['todo_items'].append(todo_item.toDictionary())

    return JsonResponse(data)