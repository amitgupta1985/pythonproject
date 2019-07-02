from django.contrib import admin

from .models import (Realtor)

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name','photo','email')

admin.site.register(Realtor,RealtorAdmin)
