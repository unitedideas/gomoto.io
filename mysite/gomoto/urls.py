from django.urls import path
from . import views
app_name = 'gomoto'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_bikes', views.get_bikes, name='get_bikes'),
]
