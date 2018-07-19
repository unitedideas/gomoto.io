from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.


# User (not seen) 1----1-> UserProfile -1----M-> UserEvent -1----M-> Event -1----M-> SpecialTests -M----1-> UserSpecialTests -M----1->|
#  ^----------------<-----------------------<------------------------<---------------------------<----------------------------------<-V


class UserProfile(models.Model):
    FEMALE = 'Female'
    MALE = 'Male'

    GENDER = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())
    birth_date = models.DateField()

    # twilio 'Lookup' API
    phone_number = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    address_line_two = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=300)

    # todo every event or keep on the user profile?
    # e_c = emergemcy contact
    e_c_name = models.CharField(max_length=300)

    # twilio 'Lookup' API
    e_c_phonenumber = models.CharField(max_length=300)


class SpecialTest(models.Model):
    special_test_num = models.CharField(max_length=300)


class UserEvent(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    bike_year = models.IntegerField()
    bike_make = models.CharField(max_length=300)
    bike_model = models.CharField(max_length=300)
    bike_displacement = models.IntegerField()

    # todo every event or put on the user profile?
    omra_number = models.IntegerField()
    ama_number = models.IntegerField()


class Event(models.Model):
    specialtest = models.ForeignKey(SpecialTest, on_delete=models.CASCADE)
    userevent = models.ForeignKey(UserEvent, on_delete=models.CASCADE)
    event_name = models.TimeField(max_length=300, null=True, blank=True)
    event_date = models.TimeField(null=True, blank=True)
    # could be added
    pro_time_est = models.TimeField(null=True, blank=True)
    am_time_est = models.TimeField(null=True, blank=True)


class UserSpecialTest(models.Model):
    specialtest = models.ForeignKey(SpecialTest, on_delete=models.CASCADE)
    start_time = models.TimeField()
    stop_time = models.TimeField()
