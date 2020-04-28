from django.contrib import admin
from .models import AccessLevels, Severities, AttachmentTypes, ReportTypes, Status, Priorities, Resolutions
# Register your models here.

admin.site.register(AccessLevels)
admin.site.register(Severities)
admin.site.register(AttachmentTypes)
admin.site.register(ReportTypes)
admin.site.register(Status)
admin.site.register(Priorities)
admin.site.register(Resolutions)