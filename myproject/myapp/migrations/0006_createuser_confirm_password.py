# Generated by Django 4.2 on 2023-08-31 09:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_createuser_confirm_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='createuser',
            name='confirm_password',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
    ]
