# Generated by Django 4.2 on 2023-09-04 11:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0009_delete_signin_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=150)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
