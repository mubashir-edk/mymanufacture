# Generated by Django 4.2 on 2023-10-17 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_quotationjob_assigned_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotationjob',
            name='assigned_employee',
        ),
        migrations.CreateModel(
            name='JobAssign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.quotationjob')),
            ],
        ),
    ]
