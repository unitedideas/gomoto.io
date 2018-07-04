from django.db import models
import datetime

# Create your models here.

class Bikes(models.Model):
    OFF_ROAD = 'Off-road'
    MOTOCROSS = 'Motocross'
    ADVENTURE = 'Adventure'
    TRIALS = 'Trials'
    MINI = 'Mini'
    TWO_STROKE = 'Two-stroke'
    FOUR_STROKE = "Four-stroke"
    ELECTRIC = "Electric"

    TYPE_OF_BIKE = (
        (OFF_ROAD, 'Off-road'),
        (MOTOCROSS, 'Motocross'),
        (ADVENTURE, 'Adventure'),
        (TRIALS, 'Trials'),
        (MINI, 'Mini'),

    )

    TYPE_OF_ENGINE = (
        (FOUR_STROKE, 'Four-stroke'),
        (TWO_STROKE, 'Two-stroke'),
        (ELECTRIC, "Electric"),


    )
    year = models.IntegerField()
    make = models.CharField(max_length=300)
    model = models.CharField(max_length=300)
    engine_type = models.CharField(max_length=300)
    weight = models.FloatField()
    displacement = models.IntegerField()
    seatheight = models.FloatField()
    price =  models.FloatField()
    horsepower =  models.FloatField()

    category = models.CharField(
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
        return self.make + " this " + self.model
