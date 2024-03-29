# Generated by Django 4.0.5 on 2023-10-24 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_user_userphotos_user_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userphotos',
            name='photo_pers_identifier',
            field=models.CharField(default=123, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userphotos',
            name='photo_secure_number',
            field=models.CharField(default=123, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
