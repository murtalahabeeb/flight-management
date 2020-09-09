# Generated by Django 3.1 on 2020-08-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0004_auto_20200823_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flight', models.ManyToManyField(blank=True, related_name='passanger', to='flight.journey')),
            ],
        ),
    ]