# Generated by Django 3.2.7 on 2021-11-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='userimages',
            name='username',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
