# Generated by Django 2.0.6 on 2018-07-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranges', '0003_auto_20180705_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='rangequestions',
            name='isdisabled',
            field=models.BooleanField(db_column='isDisabled', default=False),
        ),
    ]
