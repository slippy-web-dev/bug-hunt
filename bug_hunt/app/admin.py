from django.contrib import admin
from . import models as m
# from .models import AccessLevels, Severities, AttachmentTypes, ReportTypes, Status, Priorities, Resolutions
# Register your models here.

admin.site.register(m.Programs)
admin.site.register(m.FunctionalAreas)
admin.site.register(m.AccessLevels)
admin.site.register(m.Employees)
admin.site.register(m.ReportTypes)
admin.site.register(m.Severities)
admin.site.register(m.Status)
admin.site.register(m.Priorities)
admin.site.register(m.Resolutions)
admin.site.register(m.AttachmentTypes)
admin.site.register(m.BugReports)
admin.site.register(m.Attachments)