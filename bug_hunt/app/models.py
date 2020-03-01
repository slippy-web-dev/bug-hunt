from django.db import models

# Create your models here.
class Programs(models.Model):
    program_id      = models.AutoField(primary_key=True, max_length=11)
    program_name    = models.CharField(max_length=32)
    program_version = models.CharField(max_length=32)
    program_release = models.CharField(max_length=32)

class FunctionalAreas(models.Model):
    area_id    = models.AutoField(primary_key=True, max_length=11)
    area       = models.CharField(max_length=32)
    program_id = models.ForeignKey(Programs, on_delete=models.CASCADE)

class AccessLevels(models.Model):
    accesslevel = models.CharField(max_length=32)

class Employees(models.Model):
    employee_id          = models.AutoField(primary_key=True, max_length=11)
    employee_name        = models.CharField(max_length=32)
    employee_username    = models.CharField(max_length=32)
    employee_password    = models.CharField(max_length=32)
    employee_accesslevel = models.ForeignKey(AccessLevels, on_delete=models.CASCADE)

class ReportTypes(models.Model):
    report_type_id = models.SmallAutoField(primary_key=True, max_length=3)
    report_type    = models.CharField(max_length=32)

class Severities(models.Model):
    severity_id = models.SmallAutoField(primary_key=True, max_length=3)
    severity    = models.CharField(max_length=32)

class Status(models.Model):
    status_id = models.SmallAutoField(primary_key=True, max_length=3)
    status    = models.CharField(max_length=16)

class Priorities(models.Model):
    priority_id = models.SmallAutoField(primary_key=True, max_length=3)
    priority    = models.CharField(max_length=16)

class Resolutions(models.Model):
    resolution_id = models.SmallAutoField(primary_key=True, max_length=3)
    resolution    = models.CharField(max_length=32)

class AttachmentTypes(models.Model):
    attachment_type_id = models.SmallAutoField(primary_key=True, max_length=3)
    attachment_type    = models.CharField(max_length=32)

class BugReports(models.Model):
    bug_id             = models.AutoField(primary_key=True, max_length=11)
    program_id         = models.ForeignKey(Programs, on_delete=models.CASCADE)
    type_id            = models.ForeignKey(ReportTypes, on_delete=models.CASCADE)
    severity_id        = models.ForeignKey(Severities, on_delete=models.CASCADE)
    summary            = models.CharField(max_length=255)
    reproducable       = models.BinaryField()
    description        = models.CharField(max_length=255)
    suggested_fix      = models.CharField(max_length=255)
    reported_by_emp_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    reported_on_date   = models.DateField()
    functional_area    = models.ForeignKey(FunctionalAreas, on_delete=models.CASCADE)
    assigned_to_emp_id = models.IntegerField(max_length=11)
    comments           = models.CharField(max_length=255)
    status             = models.ForeignKey(Status, on_delete=models.CASCADE)
    priority           = models.ForeignKey(Priorities, on_delete=models.CASCADE)
    resolution         = models.ForeignKey(Resolutions, on_delete=models.CASCADE)
    resolution_version = models.SmallIntegerField(max_length=3)
    resolved_by_emp_id = models.IntegerField(max_length=11)
    resolved_on_date   = models.DateField()
    tested_by_emp_id   = models.IntegerField(max_length=11)
    tested_on_date     = models.DateField()
    treat_as_deferred  = models.BinaryField()

class Attachments(models.Model):
    attachment_id      = models.AutoField(primary_key=True, max_length=11)
    attachment_bug_id  = models.ForeignKey(BugReports, on_delete=models.CASCADE)
    attachment_type_id = models.ForeignKey(AttachmentTypes, on_delete=models.CASCADE)
    location           = models.CharField(max_length=255)
    