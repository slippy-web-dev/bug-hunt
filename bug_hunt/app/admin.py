from django.contrib import admin
from .models import Employees, FunctionalAreas, Programs, AccessLevels
# Register your models here.

admin.site.register(Employees)
admin.site.register(FunctionalAreas)
admin.site.register(Programs)
admin.site.register(AccessLevels)
