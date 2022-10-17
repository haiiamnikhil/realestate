# Generated by Django 3.2 on 2022-10-17 11:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_guestusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestusers',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]