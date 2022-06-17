from django.contrib import admin
from members.models import *

# Register your models here.

class Create_class_Admin(admin.ModelAdmin):
    list_display = ['class_id','class_name','subject_code','branch_code','college_code']
admin.site.register(Create_class,Create_class_Admin)

class Join_class_Admin(admin.ModelAdmin):
    list_display = ['class_id','user_id']
admin.site.register(Join_class)