# Generated by Django 3.2.4 on 2021-08-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FollowUp', '0005_auto_20210826_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='permanenttuitionforchild',
            name='money',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
