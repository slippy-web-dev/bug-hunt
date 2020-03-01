# Generated by Django 3.0.3 on 2020-03-01 05:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLevels',
            fields=[
                ('accessLevel_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(-1024), django.core.validators.MaxValueValidator(1023)])),
                ('accesslevel', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='AttachmentTypes',
            fields=[
                ('attachment_type_id', models.SmallAutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)])),
                ('attachment_type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Priorities',
            fields=[
                ('priority_id', models.SmallAutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)])),
                ('priority', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('program_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(-1024), django.core.validators.MaxValueValidator(1023)])),
                ('program_name', models.CharField(max_length=32)),
                ('program_version', models.CharField(max_length=32)),
                ('program_release', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ReportTypes',
            fields=[
                ('report_type_id', models.SmallAutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)])),
                ('report_type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Resolutions',
            fields=[
                ('resolution_id', models.SmallAutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)])),
                ('resolution', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Severities',
            fields=[
                ('severity_id', models.SmallAutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)])),
                ('severity', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.SmallAutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)])),
                ('status', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='FunctionalAreas',
            fields=[
                ('area_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(-1024), django.core.validators.MaxValueValidator(1023)])),
                ('area', models.CharField(max_length=32)),
                ('program_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Programs')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(-1024), django.core.validators.MaxValueValidator(1023)])),
                ('employee_name', models.CharField(max_length=32)),
                ('employee_username', models.CharField(max_length=32)),
                ('employee_password', models.CharField(max_length=32)),
                ('employee_accesslevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.AccessLevels')),
            ],
        ),
        migrations.CreateModel(
            name='BugReports',
            fields=[
                ('bug_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(-1024), django.core.validators.MaxValueValidator(1023)])),
                ('summary', models.CharField(max_length=255)),
                ('reproducable', models.BinaryField()),
                ('description', models.CharField(max_length=255)),
                ('suggested_fix', models.CharField(max_length=255)),
                ('reported_on_date', models.DateField()),
                ('assigned_to_emp_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(-1024), django.core.validators.MaxValueValidator(1023)])),
                ('comments', models.CharField(max_length=255)),
                ('resolution_version', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)])),
                ('resolved_by_emp_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(-1024), django.core.validators.MaxValueValidator(1023)])),
                ('resolved_on_date', models.DateField()),
                ('tested_by_emp_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(-1024), django.core.validators.MaxValueValidator(1023)])),
                ('tested_on_date', models.DateField()),
                ('treat_as_deferred', models.BinaryField()),
                ('functional_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.FunctionalAreas')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Priorities')),
                ('program_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Programs')),
                ('reported_by_emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Employees')),
                ('resolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Resolutions')),
                ('severity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Severities')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Status')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ReportTypes')),
            ],
        ),
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('attachment_id', models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(-1024), django.core.validators.MaxValueValidator(1023)])),
                ('location', models.CharField(max_length=255)),
                ('attachment_bug_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.BugReports')),
                ('attachment_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.AttachmentTypes')),
            ],
        ),
    ]
