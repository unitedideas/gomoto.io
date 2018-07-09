
from import_export import resources
from django.contrib import admin
from .models import Bike
from core.models import Bike
# Register your models here.



admin.site.register(Bike)



class BookResource(resources.ModelResource):

    class Meta:
        model = Book