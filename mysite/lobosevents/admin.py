from django.contrib import admin
from .models import Profile, UserEvent, Event, SpecialTest, UserSpecialTest

# Register your models here.
admin.site.register(Profile)
admin.site.register(UserEvent)
admin.site.register(Event)
admin.site.register(SpecialTest)
admin.site.register(UserSpecialTest)

