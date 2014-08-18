from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Member(AbstractUser):
    MALE = 'm'
    FEMALE = 'f'
    OTHER = 'o'
    options = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )
    airport = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=options)
    age = models.PositiveIntegerField(null=True)


    def __unicode__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=35)
    user = models.ForeignKey(Member, related_name='category_user')

    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=20, blank=False)
    category = models.ForeignKey(Category, related_name='event_category')

    def __unicode__(self):
        return self.name