# Generated by Django 2.2.7 on 2019-12-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='website',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]