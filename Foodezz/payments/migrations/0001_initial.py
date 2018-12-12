# Generated by Django 2.1.3 on 2018-12-12 11:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hotel', '0003_auto_20181212_1643'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=150)),
                ('status', models.CharField(default='buylater', max_length=50)),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('restaurantid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Hotel.RestaurantLog')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(max_length=12)),
                ('deliveryid', models.CharField(max_length=12)),
                ('foodname', models.CharField(max_length=150)),
                ('quantity', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=5)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(max_length=150)),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('restaurantid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Hotel.RestaurantLog')),
            ],
        ),
    ]