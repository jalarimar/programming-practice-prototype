# Generated by Django 2.0.4 on 2018-09-01 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0022_auto_20180902_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earned',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='loginday',
            name='day',
            field=models.DateField(),
        ),
    ]