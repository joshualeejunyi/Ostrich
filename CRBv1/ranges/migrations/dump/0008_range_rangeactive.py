# Generated by Django 2.0.5 on 2018-05-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranges', '0007_auto_20180526_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='range',
            name='rangeactive',
            field=models.BooleanField(db_column='rangeActive', default=False),
        ),
    ]