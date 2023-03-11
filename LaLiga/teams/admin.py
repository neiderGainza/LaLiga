from django.contrib import admin

# Register your models here.

from . import models 

admin.site.register(models.Team)
admin.site.register(models.Game)
admin.site.register(models.Goal)
admin.site.register(models.Yelow_Card)
admin.site.register(models.Red_Card)
