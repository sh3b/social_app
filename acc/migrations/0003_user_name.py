# Generated by Django 2.2.7 on 2019-12-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0002_auto_20191202_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]