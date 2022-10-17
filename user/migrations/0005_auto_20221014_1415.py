# Generated by Django 3.2 on 2022-10-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20221014_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
