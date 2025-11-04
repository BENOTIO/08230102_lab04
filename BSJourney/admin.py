from django.contrib import admin
from .models import LearningJourney, AboutMe

class LearningJourneyAdmin(admin.ModelAdmin):
    list_display = ['title']  # remove 'date' if it doesn't exist

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name']  # remove 'user' if it doesn't exist

admin.site.register(LearningJourney, LearningJourneyAdmin)
admin.site.register(AboutMe, AboutMeAdmin)
