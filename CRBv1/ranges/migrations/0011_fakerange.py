# Generated by Django 2.0.6 on 2018-07-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranges', '0010_auto_20180710_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='FakeRange',
            fields=[
                ('rangeid', models.AutoField(db_column='rangeID', primary_key=True, serialize=False)),
                ('rangename', models.CharField(db_column='rangeName', max_length=45)),
                ('rangeactive', models.BooleanField(db_column='rangeActive', default=False)),
                ('datecreated', models.DateField(blank=True, db_column='dateCreated', null=True)),
                ('datestart', models.DateField(blank=True, db_column='dateStart', null=True)),
                ('timestart', models.TimeField(blank=True, db_column='timeStart', null=True)),
                ('dateend', models.DateField(blank=True, db_column='dateEnd', null=True)),
                ('timeend', models.TimeField(blank=True, db_column='timeEnd', null=True)),
                ('maxscore', models.IntegerField(blank=True, db_column='maxScore', null=True)),
                ('lastmodifieddate', models.DateField(blank=True, db_column='lastModifiedDate', null=True)),
                ('rangecode', models.IntegerField(blank=True, db_column='rangeCode', null=True, unique=True)),
                ('rangeurl', models.CharField(db_column='rangeURL', max_length=50, null=True, unique=True)),
                ('studentsinrange', models.IntegerField(db_column='studentsInRange', null=True)),
                ('isdisabled', models.BooleanField(db_column='isDisabled', default=False)),
            ],
            options={
                'managed': False,
                'db_table': 'Range',
            },
        ),
    ]
