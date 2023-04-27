from django.contrib import admin
from app1.models import *

# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['tname','phno']

@admin.register(info)
class infoAdmin(admin.ModelAdmin):
    list_display=['sname','subject']
