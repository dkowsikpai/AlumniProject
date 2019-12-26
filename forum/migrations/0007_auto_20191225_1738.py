# Generated by Django 2.2.7 on 2019-12-25 17:38

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_posts_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image1',
            field=image_optimizer.fields.OptimizedImageField(default='default.png', upload_to='projects'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image2',
            field=image_optimizer.fields.OptimizedImageField(blank=True, upload_to='projects'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image3',
            field=image_optimizer.fields.OptimizedImageField(blank=True, upload_to='projects'),
        ),
    ]