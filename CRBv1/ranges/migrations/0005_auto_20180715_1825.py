# Generated by Django 2.0.6 on 2018-07-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranges', '0004_questions_isarchived'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='marks',
        ),
        migrations.AddField(
            model_name='questions',
            name='points',
            field=models.PositiveIntegerField(db_column='points', default=0),
        ),
    ]
