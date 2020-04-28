# Generated by Django 3.0.3 on 2020-04-27 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugreports',
            name='assigned_to_emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_emp', to='app.Employees'),
        ),
        migrations.AlterField(
            model_name='bugreports',
            name='reported_by_emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_emp', to='app.Employees'),
        ),
        migrations.AlterField(
            model_name='bugreports',
            name='reproducable',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='bugreports',
            name='resolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resol', to='app.Resolutions'),
        ),
        migrations.AlterField(
            model_name='bugreports',
            name='resolution_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resol_version', to='app.Resolutions'),
        ),
        migrations.AlterField(
            model_name='bugreports',
            name='resolved_by_emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resolved_emp', to='app.Employees'),
        ),
        migrations.AlterField(
            model_name='bugreports',
            name='tested_by_emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tested_emp', to='app.Employees'),
        ),
        migrations.AlterField(
            model_name='bugreports',
            name='treat_as_deferred',
            field=models.BooleanField(),
        ),
    ]
