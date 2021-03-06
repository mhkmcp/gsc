# Generated by Django 3.1.3 on 2021-03-23 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('src', '0002_auto_20210321_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(default='', upload_to='img/members'),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
    ]
