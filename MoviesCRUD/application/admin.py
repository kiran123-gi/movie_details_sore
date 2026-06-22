from django.contrib import admin
from .models import movies

class moviesAdmin(admin.ModelAdmin):
    list_display = ['sno','name','hero','heroine','director','music','year']
admin.site.register(movies,moviesAdmin)
