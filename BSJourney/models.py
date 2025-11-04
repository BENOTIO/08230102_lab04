from django.db import models

class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # add date if you want to use it in admin
    date = models.DateField(auto_now_add=True)

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    # add user if needed
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
