# Generated by Django 4.2.1 on 2023-05-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nyaa_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchentry',
            name='language',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='searchentry',
            name='trad_team',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
