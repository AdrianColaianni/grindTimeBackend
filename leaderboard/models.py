from django.db import models

# Create your models here.
class CUser(models.Model):
    user_name = models.CharField(max_length=100, null=False)

class Building(models.Model):
    id = models.PositiveIntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=100, null=False)

class Score(models.Model):
    user = models.ForeignKey(to=CUser, on_delete=models.CASCADE, blank=False, null=False)
    duration = models.DurationField(blank=False, null=False)
    time = models.DateTimeField(blank=False, null=False)
