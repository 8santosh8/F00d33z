# Generated by Django 2.1.3 on 2018-11-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orderscarrying',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(max_length=150)),
                ('driverid', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='presentlocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driverid', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
            ],
        ),
    ]