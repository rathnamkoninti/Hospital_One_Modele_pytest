from django.contrib import admin
from .models import Hospital
# Register your models here.
class HospitalModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile']
admin.site.register(Hospital,HospitalModelAdmin)