# Generated by Django 3.2 on 2022-10-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='rooms',
            field=models.CharField(blank=True, default='1', max_length=20, null=True),
        ),
    ]