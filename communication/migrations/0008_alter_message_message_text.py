# Generated by Django 3.2.4 on 2021-08-01 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0007_auto_20210728_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_text',
            field=models.CharField(max_length=40),
        ),
    ]
