from django.contrib import admin
from .models import Table

# Register your models here.
# admin.site.register(Table)

@admin.register(Table)
class abc(admin.ModelAdmin):
    list_display = ['id','name','age','city']

