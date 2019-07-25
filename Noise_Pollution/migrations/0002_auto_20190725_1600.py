# Generated by Django 2.2.3 on 2019-07-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noise_Pollution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dati',
            name='analogic_value',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='dati',
            name='digital_value',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='dati',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='dati',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]