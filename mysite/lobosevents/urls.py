from django.urls import path, include

from mysite.lobosevents.templates.lobosevents import views

app_name = 'todo'

urlpatterns = [

    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('login_register/', views.login_register, name='login_register'),
    path('removed_item/', views.remove_todo, name='todo_remove_unicorn'),
    path('login/', views.mylogin, name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('register/', views.register, name='register'),
]
