# Generated by Django 2.0.4 on 2018-09-22 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0027_auto_20180922_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='id_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]