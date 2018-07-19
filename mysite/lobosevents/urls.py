from django.urls import path, include

from . import views

app_name = 'lobosevents'

urlpatterns = [

    path('index/', views.index, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login_register/', views.login_register, name='login_register'),
    path('login/', views.mylogin, name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('register/', views.register, name='register'),

]
