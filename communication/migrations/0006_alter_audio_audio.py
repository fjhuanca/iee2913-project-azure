# Generated by Django 3.2.4 on 2021-07-27 20:17

import communication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0005_alter_audio_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio',
            field=models.FileField(upload_to=communication.models.upload_root_gen),
        ),
    ]
