# Generated by Django 2.0.6 on 2018-07-10 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranges', '0008_auto_20180710_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='rangequestions',
            name='registryid',
            field=models.CharField(db_column='registryID', max_length=255, null=True),
        ),
    ]
