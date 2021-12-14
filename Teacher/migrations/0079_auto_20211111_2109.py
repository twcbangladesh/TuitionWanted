# Generated by Django 3.2.4 on 2021-11-11 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0078_auto_20211108_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('SHORT', models.CharField(blank=True, max_length=10, null=True)),
                ('URL', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['Name'],
            },
        ),
        migrations.AlterField(
            model_name='thana',
            name='District',
            field=models.ForeignKey(default=70, on_delete=django.db.models.deletion.CASCADE, to='Teacher.district'),
        ),
    ]
