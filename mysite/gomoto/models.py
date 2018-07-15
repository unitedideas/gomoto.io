from django.db import models
import datetime

# Create your models here.


class Bike(models.Model):
    OFF_ROAD = 'Off-Road'
    MOTOCROSS = 'Motocross'
    ADVENTURE = 'Adventure'
    TRIALS = 'Trials'
    MINI = 'Mini'
    ENDURO = 'Enduro'
    TWO_STROKE = 'Two-stroke'
    FOUR_STROKE = "Four-stroke"
    ELECTRIC = "Electric"

    TYPE_OF_BIKE = (
        (OFF_ROAD, 'Off-Road'),
        (MOTOCROSS, 'Motocross'),
        (ADVENTURE, 'Adventure'),
        (TRIALS, 'Trials'),
        (MINI, 'Mini'),
        (ENDURO, 'Enduro'),

    )

    TYPE_OF_ENGINE = (
        (FOUR_STROKE, 'Four-stroke'),
        (TWO_STROKE, 'Two-stroke'),
        (ELECTRIC, "Electric"),

    )

    # {'img_src': 'https://www.dirtrider.com/sites/dirtrider.com/files/styles/1000_1x_/public/buyers_guide/2019/2018_Kawasaki_KLX_140G.jpg?itok=us-b03Ng',
    # 'price': 3699, 'displacement': 144, 'seatheight': 34, 'wet_weight': 218, 'dry_weight': None,
    # 'starter': 'Electric', 'category': 'Off-Road', 'engine_type': 'SOHC', 'year': 2019,
    # 'make': 'Kawasaki', 'model': 'Klx140G'}

    year = models.IntegerField(null=True, blank=True)
    make = models.CharField(max_length=300, null=True, blank=True)
    model = models.CharField(max_length=300, null=True, blank=True)
    price =  models.FloatField(null=True, blank=True)
    starter = models.CharField(max_length=300,null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    displacement = models.IntegerField(null=True, blank=True)
    seatheight = models.FloatField(null=True, blank=True)
    img_src = models.CharField(max_length=300, null=True, blank=True)


    category = models.CharField(
        null=True, blank=True,
        max_length=300,
        choices=TYPE_OF_BIKE,
        default=OFF_ROAD,
    )

    engine_type = models.CharField(
        max_length=300,
        choices=TYPE_OF_ENGINE,
        default=FOUR_STROKE,
    )


    def __str__(self):
        return str(self.year) + ' ' + self.make + " " + self.model


    def top_3_bikes(self):
        return {'text': self.text}




















