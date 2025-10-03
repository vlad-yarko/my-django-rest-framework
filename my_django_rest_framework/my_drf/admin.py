from django.contrib import admin
from .models import Cucumber


class CucumberAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cucumber, CucumberAdmin)
