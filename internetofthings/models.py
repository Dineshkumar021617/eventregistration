from django.db import models
from django.contrib import admin

# Create your models here.

class Participant(models.Model):
    name = models.CharField(max_length=100)
    phoneno = models.IntegerField()
    email = models.CharField(max_length=100)
    institutionname = models.CharField(max_length=100)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name','phoneno','email','institutionname')