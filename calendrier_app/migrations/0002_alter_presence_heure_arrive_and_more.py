# Generated by Django 4.2.7 on 2024-09-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendrier_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presence',
            name='heure_arrive',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='presence',
            name='heure_depart',
            field=models.TimeField(blank=True, null=True),
        ),
    ]