from django.contrib import admin

# Register your models here.

from .import models

admin.site.register(models.Players)
admin.site.register(models.Belong)