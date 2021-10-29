# Generated by Django 3.2.7 on 2021-10-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0002_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trolly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('sub_name', models.CharField(blank=True, max_length=254, null=True)),
                ('sub_display_name', models.CharField(blank=True, max_length=254, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.AddField(
            model_name='subscription',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]