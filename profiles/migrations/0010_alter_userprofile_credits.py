# Generated by Django 3.2.7 on 2021-11-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20211120_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='credits',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
