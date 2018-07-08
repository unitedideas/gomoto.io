from django.db import models
import datetime

# Create your models here.

class Bike(models.Model):
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

    year = models.IntegerField(null=True, blank=True)
    make = models.CharField(max_length=300, null=True, blank=True)
    model = models.CharField(max_length=300, null=True, blank=True)
    price =  models.FloatField(null=True, blank=True)
    starter = models.CharField(max_length=300)
    #for nullable values
    dry_weight = models.FloatField(null=True, blank=True)
    wet_weight = models.FloatField(null=True, blank=True)
    displacement = models.IntegerField(null=True, blank=True)
    seatheight = models.FloatField()


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
        return self.make + " " + self.model
