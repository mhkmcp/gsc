# Generated by Django 3.1.3 on 2021-03-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_auto_20210323_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='year',
            field=models.IntegerField(default='2021'),
        ),
    ]
