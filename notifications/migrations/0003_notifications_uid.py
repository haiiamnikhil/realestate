# Generated by Django 3.2 on 2022-10-17 11:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_notifications_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
