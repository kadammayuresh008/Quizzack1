# Generated by Django 3.1.1 on 2021-02-05 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20210203_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='hint',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='attempts',
            name='attemptedtime',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 12, 19, 50, 845006)),
        ),
    ]
