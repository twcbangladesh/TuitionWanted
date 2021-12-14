# Generated by Django 3.2.4 on 2021-08-26 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuardianArea', '0010_auto_20210825_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='Expected_Day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='Education_Level',
            field=models.SmallIntegerField(choices=[(0, 'Class 0'), (1, 'Class 1'), (2, 'Class 2'), (3, 'Class 3'), (4, 'Class 4'), (5, 'Class 5'), (6, 'Class 6'), (7, 'Class 7'), (8, 'Class 8'), (9, 'Class 9'), (10, 'Class 10'), (11, 'Class 11'), (12, 'Class 10'), (13, 'Diploma'), (14, 'Degree'), (15, 'Honors'), (16, 'O-Level'), (17, 'A-Level(AS)'), (19, 'pre-KG'), (17, 'KG'), (18, 'A-Level(A2)'), (20, 'Others')], default=20),
        ),
        migrations.AlterField(
            model_name='child',
            name='Education_Medium',
            field=models.SmallIntegerField(choices=[(1, 'Bangla Medium'), (2, 'English Medium'), (3, 'English Version'), (4, 'Madrasa Medium'), (7, 'Others')], default=1),
        ),
        migrations.AlterField(
            model_name='child',
            name='slug',
            field=models.SlugField(default='bobp', help_text='Do not change it', max_length=5, primary_key=True, serialize=False),
        ),
    ]
