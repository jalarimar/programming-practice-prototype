# Generated by Django 2.0.4 on 2018-09-22 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0026_profile_goal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='badge',
            old_name='name',
            new_name='display_name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
