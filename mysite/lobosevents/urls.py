from django.urls import path, include

from . import views

app_name = 'lobosevents'

urlpatterns = [

    path('index/', views.index, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
]
