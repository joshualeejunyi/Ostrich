# Generated by Django 2.0.5 on 2018-05-25 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ranges', '0003_auto_20180525_0746'),
    ]

    operations = [
        migrations.CreateModel(
            name='RangeStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateJoined', models.DateTimeField(blank=True, db_column='dateJoined', max_length=45, null=True)),
                ('progress', models.CharField(db_column='progress', max_length=45)),
                ('teamID', models.CharField(db_column='teamID', max_length=45)),
                ('teamName', models.CharField(db_column='teamName', max_length=45)),
                ('points', models.IntegerField(db_column='points')),
                ('rangeID', models.ForeignKey(db_column='rangeID', on_delete=django.db.models.deletion.DO_NOTHING, to='ranges.Range', unique=True)),
                ('studentID', models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]