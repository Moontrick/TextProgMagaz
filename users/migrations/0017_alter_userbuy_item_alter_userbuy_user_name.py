# Generated by Django 4.0.5 on 2024-02-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_userbuy_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbuy',
            name='item',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='userbuy',
            name='user_name',
            field=models.IntegerField(max_length=255),
        ),
    ]
