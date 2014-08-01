from django.contrib import admin

# Register your models here.
from finder.models import *

admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Category)