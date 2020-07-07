from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_per_page = 20

# Register your models here.
admin.site.register(Realtor, RealtorAdmin)
# Register your models here.
