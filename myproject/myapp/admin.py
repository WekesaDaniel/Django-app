from django.contrib import admin
from.models import UserDetail

# Register your models here.
admin.site.register(UserDetail)

# Item model register
from .models import Item

admin.site.register(Item)
