from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=35)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    category = models.ForeignKey(Category, related_name='event_category')

    def __unicode__(self):
        return self.category.name

class Member(AbstractUser):
    MALE = 'm'
    FEMALE = 'f'
    OTHER = 'o'
    options = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )
    airport = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=10, choices=options)
    age = models.PositiveIntegerField(null=True)
    event = models.ForeignKey(Event, blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.username)




