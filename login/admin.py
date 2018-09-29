from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.M_User)
admin.site.register(models.M_Confirm)
