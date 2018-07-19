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
    user = models.ForeignKey(User,  null=True, blank=True, on_delete=models.CASCADE)
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())
    birth_date = models.CharField(max_length=300, null=True, blank=True)

    # twilio 'Lookup' API
    phone_number = models.CharField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=300, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    address_line_two = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)
    state = models.CharField(max_length=300, null=True, blank=True)
    zip_code = models.CharField(max_length=300, null=True, blank=True)

    # todo every event or keep on the user profile?
    # e_c = emergemcy contact
    e_c_name = models.CharField(max_length=300, null=True, blank=True)

    # twilio 'Lookup' API
    e_c_phonenumber = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.user) + ' Contact Info'


class Event(models.Model):
    event_name = models.CharField(max_length=300, null=True, blank=True)
    event_date = models.DateField(max_length=300, null=True, blank=True)
    # could be added
    pro_time_est = models.TimeField(max_length=300, null=True, blank=True)
    am_time_est = models.TimeField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.event_name) + ' ' + str(self.event_date)


class SpecialTest(models.Model):
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.CASCADE)
    special_test_num = models.IntegerField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.event) + ' Special Tests ' + str(self.special_test_num)


class UserEvent(models.Model):
    event = models.ForeignKey(Event,  null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User,   null=True, blank=True, on_delete=models.CASCADE)
    bike_year = models.IntegerField(null=True, blank=True)
    bike_make = models.CharField(max_length=300, null=True, blank=True)
    bike_model = models.CharField(max_length=300, null=True, blank=True)
    bike_displacement = models.IntegerField(null=True, blank=True)
    placard = models.IntegerField(null=True, blank=True)

    # todo every event or put on the user profile?
    omra_number = models.IntegerField()
    ama_number = models.IntegerField()

    def __str__(self):
        return str(self.user) + ' - ' + str(self.placard)




class UserSpecialTest(models.Model):
    specialtest = models.ForeignKey(SpecialTest, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=300, null=True, blank=True)
    stop_time = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.specialtest.event)

