from django.db import models
import birthday


# Create your models here.


# User (not seen) 1----1-> UserProfile -1----M-> UserEvent -1----M-> Event -1----M-> SpecialTests -M----1-> UserSpecialTests -M----1->|
#  ^----------------<-----------------------<------------------------<---------------------------<----------------------------------<-V

class UserProfile(models.Model):
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())
    birth_date = models.DateField()

    # twilio 'Lookup' API
    phone_number = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    address_line_two = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=300)

    # e_c = emergemcy contact
    e_c_name = models.CharField(max_length=300)

    # twilio 'Lookup' API
    e_c_phonenumber = models.CharField(max_length=300)
    address = models.CharField(max_length=300)



class





















