from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .decorators import check_recaptcha
from django.conf import settings
from django.contrib import messages
import json
import urllib

from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from statistics import *
from datetime import time
from cmath import sqrt
from collections import OrderedDict
import json, numpy, importlib, datetime, operator
from django.db.models import Avg, Max, Min, Sum
from .models import Profile, UserEvent
from django.conf import settings
from django.contrib import messages
import json
import urllib


def index(request):
    return HttpResponse("Hello, world. You're at the lobos registration page.")


# @login_required
def event_registration(request):
    pass
    # todo_text = request.POST['todo_item_id_key_in_template']
    # todo_item = TodoItem.objects.get(pk=todo_text)
    # todo_item.delete()
    # # item_on_list = question.choice_set.get(pk=request.POST['choice'])
    # # save data from request.POST in database
    # # redirect back to the index page (HttpResponseRedirect)
    #
    # return HttpResponseRedirect(reverse('lobosevents:event_registration'))

def profile(request):
    logout(request)
    return HttpResponseRedirect(reverse('lobosevents:profile'))

@check_recaptcha
def register(request):
    if not request.recaptcha_is_valid:
        return HttpResponseRedirect(reverse('lobosevents:login_register')+'?message=bad_recaptcha')
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('lobosevents:index'))


@check_recaptcha
def mylogin(request):
    if not request.recaptcha_is_valid:
        return HttpResponseRedirect(reverse('lobosevents:login_register')+'?message=bad_recaptcha')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)


    if user is not None:
        login(request, user)
        if 'next' in request.POST and request.POST['next'] != '':
            return HttpResponseRedirect(request.POST['next'])
        return HttpResponseRedirect(reverse('lobosevents:index'))
    return HttpResponseRedirect(reverse('lobosevents:login_register'))


def mylogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('lobosevents:login_register'))



def login_register(request):
    message = request.GET.get('message', '')
    next = request.GET.get('next', '')
    return render(request, 'lobosevents/login_register.html', {'next': next, 'message': message})
