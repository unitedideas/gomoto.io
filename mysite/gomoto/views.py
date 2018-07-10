from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import json
from .models import Bike

def index(request):
    return render(request, 'gomoto/index.html', {})


