# Generated by Django 2.1.2 on 2018-11-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='restrict_comment',
            field=models.BooleanField(default=False),
        ),
    ]