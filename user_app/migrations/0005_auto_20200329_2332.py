# Generated by Django 3.0.3 on 2020-03-29 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_auto_20200329_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='end_time',
            field=models.CharField(default='Mar 29 2020 23:32:01', max_length=50),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.CharField(default='Mar 29 2020 23:32:01', max_length=50),
        ),
    ]
