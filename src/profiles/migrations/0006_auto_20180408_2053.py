# Generated by Django 2.1.dev20180328172503 on 2018-04-08 16:53

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20180408_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='location',
            new_name='city',
        ),
        migrations.AddField(
            model_name='student',
            name='country',
            field=models.CharField(default='city', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_image_path),
        ),
    ]
