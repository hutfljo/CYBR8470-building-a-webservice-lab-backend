from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin

from rest_framework import serializers

import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')



class Breed(models.Model):


    SIZES = (
        ('tiny', 'Tiny'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('Tiny', 'tiny'),
        ('Small', 'small'),
        ('Medium', 'medium'),
        ('Large', 'large')
    )

    NUMBER_CHOICES = (
        (1, 1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )

    name = models.CharField(max_length=30)
    size = models.CharField(max_length=6, choices=SIZES)
    friendliness = models.IntegerField(choices=NUMBER_CHOICES)
    trainability = models.IntegerField(choices=NUMBER_CHOICES)
    sheddingamount = models.IntegerField(choices=NUMBER_CHOICES)
    exerciseneeds = models.IntegerField(choices=NUMBER_CHOICES)

    def __str__(self):
        return str(self.name)

class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1)
    color = models.CharField(max_length=20)
    favoriteFood = models.CharField(max_length=50)
    favoriteToy = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
