# Generated by Django 4.1.4 on 2022-12-10 08:18

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to=authentication.models.path_to_avatar
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
