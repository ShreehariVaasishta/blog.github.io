# Generated by Django 2.1.7 on 2019-05-16 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_title1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title1',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
