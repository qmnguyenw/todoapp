# Generated by Django 3.0.2 on 2020-01-15 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoAppAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
