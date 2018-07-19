from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Profile, UserEvent, Event, SpecialTest, UserSpecialTest, Person

# Register your models here.
admin.site.register(Profile)
admin.site.register(UserEvent)
admin.site.register(Event)
admin.site.register(SpecialTest)
admin.site.register(UserSpecialTest)

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass