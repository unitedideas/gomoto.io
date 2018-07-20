from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .decorators import check_recaptcha
from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from tablib import Dataset
from .resources import PersonResource
from django.core.mail import send_mail


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
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )

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


def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')




send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)




















