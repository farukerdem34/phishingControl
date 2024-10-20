from django.contrib import admin
from .models import Name

class ModelAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name')

admin.site.register(Name,ModelAdmin)
