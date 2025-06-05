from django.contrib import admin
from myapp.models import *
# Register your models here.

class category(admin.ModelAdmin):
    list_display = ['id','category_name']



admin.site.register(Category, category)
admin.site.register(Disease)
admin.site.register(Item)

