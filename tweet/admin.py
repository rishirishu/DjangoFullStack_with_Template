from django.contrib import admin
from .models import *

# Register your models here.

# class TweetAdmin(admin.ModelAdmin):
#     class Meta:
#         models = Tweet
#         list_display =['user','tweet']

admin.site.register(Tweet)
# admin.site.register(Tweet)