from django.contrib import admin

# Register your models here.
from.models import Blogpost

from django.contrib.admin import  ModelAdmin

from.models import  *


@admin.register(Blogpost)
class MainAdmin(admin.ModelAdmin):
      list_display = ['title','content','image']


admin.site.register(Comment)