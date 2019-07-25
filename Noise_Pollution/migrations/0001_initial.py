# Generated by Django 2.2.3 on 2019-07-25 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensore',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.BooleanField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dati',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('sensore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Noise_Pollution.Sensore')),
            ],
        ),
    ]