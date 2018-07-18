from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the lobos index.")


@login_required
def user(request):
    todo_text = request.POST['todo_item_id_key_in_template']
    todo_item = TodoItem.objects.get(pk=todo_text)
    todo_item.delete()
    # item_on_list = question.choice_set.get(pk=request.POST['choice'])
    # save data from request.POST in database
    # redirect back to the index page (HttpResponseRedirect)

    return HttpResponseRedirect(reverse('todo:index'))

@check_recaptcha
def register(request):
    if not request.recaptcha_is_valid:
        return HttpResponseRedirect(reverse('todo:login_register')+'?message=bad_recaptcha')
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('todo:index'))


@check_recaptcha
def mylogin(request):
    if not request.recaptcha_is_valid:
        return HttpResponseRedirect(reverse('todo:login_register')+'?message=bad_recaptcha')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)


    if user is not None:
        login(request, user)
        if 'next' in request.POST and request.POST['next'] != '':
            return HttpResponseRedirect(request.POST['next'])
        return HttpResponseRedirect(reverse('todo:index'))
    return HttpResponseRedirect(reverse('todo:login_register'))


def mylogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('todo:login_register'))



def login_register(request):
    message = request.GET.get('message', '')
    next = request.GET.get('next', '')
    return render(request, 'todo/login_register.html', {'next': next, 'message': message})
