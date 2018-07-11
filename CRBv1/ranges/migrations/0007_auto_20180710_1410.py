# Generated by Django 2.0.6 on 2018-07-10 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ranges', '0006_auto_20180709_1209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='range',
            options={'ordering': ['-rangeid'], 'verbose_name_plural': 'Ranges'},
        ),
        migrations.AddField(
            model_name='questions',
            name='createdby',
            field=models.ForeignKey(db_column='createdby', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='questioncreatedby', to=settings.AUTH_USER_MODEL),
        ),
    ]
