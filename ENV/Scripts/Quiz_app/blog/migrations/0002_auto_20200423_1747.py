# Generated by Django 3.0.5 on 2020-04-23 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='option1',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option4',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='question',
        ),
    ]
