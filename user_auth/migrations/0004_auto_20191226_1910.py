# Generated by Django 2.2.7 on 2019-12-26 19:10

from django.db import migrations, models
import user_auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_profile_batch_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='batch_year',
            field=models.IntegerField(default=user_auth.models.current_year, verbose_name='Year'),
        ),
    ]
