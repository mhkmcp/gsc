# Generated by Django 3.1.3 on 2021-03-21 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='full_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='member',
            name='passport',
            field=models.CharField(default='', max_length=63),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_type',
            field=models.CharField(choices=[('g', 'General Member'), ('l', 'Lifetime Member'), ('a', 'Admin')], default='', max_length=24),
        ),
    ]
