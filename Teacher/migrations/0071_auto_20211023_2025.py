# Generated by Django 3.2.4 on 2021-10-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0070_auto_20211023_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='Name',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='thana',
            name='Name',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
