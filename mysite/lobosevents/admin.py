from django.contrib import admin
from .models import UserProfile, UserEvent, Event, SpecialTest, UserSpecialTest
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserEvent)
admin.site.register(Event)
admin.site.register(SpecialTest)
admin.site.register(UserSpecialTest)


