from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Programs(models.Model):
    program_id      = models.AutoField(primary_key=True, validators=[MinValueValidator(-1024),MaxValueValidator(1023)])
    program_name    = models.CharField(max_length=32)
    program_version = models.CharField(max_length=32)
    program_release = models.CharField(max_length=32)
    objects = models.Manager()

    def __str__(self):
        return self.program_name

    
class FunctionalAreas(models.Model):
    area_id    = models.AutoField(primary_key=True, validators=[MinValueValidator(-1024),MaxValueValidator(1023)])
    area       = models.CharField(max_length=32)
    program_id = models.ForeignKey('Programs', on_delete=models.CASCADE)
    objects = models.Manager()

class AccessLevels(models.Model):
    accessLevel_id = models.AutoField(primary_key=True, validators=[MinValueValidator(-1024),MaxValueValidator(1023)])
    accesslevel = models.CharField(max_length=32)
    objects = models.Manager()

class Employees(models.Model):
    employee_id          = models.AutoField(primary_key=True, validators=[MinValueValidator(-1024),MaxValueValidator(1023)])
    employee_name        = models.CharField(max_length=32)
    employee_username    = models.CharField(max_length=32)
    employee_password    = models.CharField(max_length=32)
    employee_accesslevel = models.ForeignKey('AccessLevels', on_delete=models.CASCADE)
    objects = models.Manager()

class ReportTypes(models.Model):
    report_type_id = models.SmallAutoField(primary_key=True, validators=[MinValueValidator(0),MaxValueValidator(8)])
    report_type    = models.CharField(max_length=32)
    objects = models.Manager()

class Severities(models.Model):
    severity_id = models.SmallAutoField(primary_key=True, validators=[MinValueValidator(0),MaxValueValidator(8)])
    severity    = models.CharField(max_length=32)
    objects = models.Manager()

class Status(models.Model):
    status_id = models.SmallAutoField(primary_key=True, validators=[MinValueValidator(0),MaxValueValidator(8)])
    status    = models.CharField(max_length=16)
    objects = models.Manager()

class Priorities(models.Model):
    priority_id = models.SmallAutoField(primary_key=True, validators=[MinValueValidator(0),MaxValueValidator(8)])
    priority    = models.CharField(max_length=16)
    objects = models.Manager()

class Resolutions(models.Model):
    resolution_id = models.SmallAutoField(primary_key=True, validators=[MinValueValidator(0),MaxValueValidator(8)])
    resolution    = models.CharField(max_length=32)
    objects = models.Manager()

# class AttachmentTypes(models.Model):
#     attachment_type_id = models.SmallAutoField(primary_key=True, validators=[MinValueValidator(0),MaxValueValidator(8)])
#     attachment_type    = models.CharField(max_length=32)
#     objects = models.Manager()

class BugReports(models.Model):
    bug_id             = models.AutoField(primary_key=True, validators=[MinValueValidator(-1024),MaxValueValidator(1023)])
    program_id         = models.ForeignKey('Programs', on_delete=models.CASCADE)
    type_id            = models.ForeignKey('ReportTypes', on_delete=models.CASCADE)
    severity_id        = models.ForeignKey('Severities', on_delete=models.CASCADE)
    summary            = models.CharField(max_length=255)
    reproducable       = models.BooleanField()
    description        = models.CharField(max_length=255)
    suggested_fix      = models.CharField(max_length=255)
    reported_by_emp_id = models.ForeignKey('Employees', on_delete=models.CASCADE, related_name="reported_emp")
    reported_on_date   = models.DateField()
    functional_area    = models.ForeignKey('FunctionalAreas', on_delete=models.CASCADE, null=True, blank=True)
    assigned_to_emp_id = models.ForeignKey('Employees', on_delete=models.CASCADE,related_name="assigned_emp", null=True, blank=True)
    comments           = models.CharField(max_length=255, blank=True)
    status             = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, blank=True)
    priority           = models.ForeignKey('Priorities', on_delete=models.CASCADE, null=True, blank=True)
    resolution         = models.ForeignKey('Resolutions', on_delete=models.CASCADE, related_name="resol", null=True, blank=True)
    resolution_version = models.ForeignKey('Resolutions', on_delete=models.CASCADE, related_name="resol_version", null=True, blank=True)
    resolved_by_emp_id = models.ForeignKey('Employees', on_delete=models.CASCADE, related_name="resolved_emp", null=True, blank=True)
    resolved_on_date   = models.DateField(null=True, blank=True)
    tested_by_emp_id   = models.ForeignKey('Employees', on_delete=models.CASCADE, related_name="tested_emp", null=True, blank=True)
    tested_on_date     = models.DateField(null=True, blank=True)
    treat_as_deferred  = models.BooleanField()
    attachment         = models.ForeignKey('Attachments', on_delete=models.CASCADE, null=True, blank=True)
    objects = models.Manager()

        

class Attachments(models.Model):
    attachment_id      = models.AutoField(primary_key=True, validators=[MinValueValidator(-1024),MaxValueValidator(1023)])
    attachment_bug_id  = models.ForeignKey('BugReports', on_delete=models.CASCADE)
    # attachment_type_id = models.ForeignKey('AttachmentTypes', on_delete=models.CASCADE)
    attachment_name    = models.CharField(max_length=255, default='')
    location           = models.CharField(max_length=255, default='')
    objects = models.Manager()
    