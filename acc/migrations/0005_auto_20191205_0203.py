# Generated by Django 2.2.7 on 2019-12-04 22:03

import acc.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0004_auto_20191205_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=acc.models.User.get_avatar_file_path),
        ),
    ]