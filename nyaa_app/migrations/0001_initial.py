# Generated by Django 4.2.1 on 2023-05-14 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('episode', models.IntegerField()),
                ('season', models.IntegerField()),
                ('language', models.CharField(max_length=200)),
                ('trad_team', models.CharField(max_length=200)),
                ('quality', models.CharField(choices=[('480p', 'Q480P'), ('720p', 'Q720P'), ('1080p', 'Q1080P')], default='1080p', max_length=200)),
                ('video_format', models.CharField(choices=[('mkv', 'Mkv'), ('mp4', 'Mp4')], default='mkv', max_length=200)),
            ],
        ),
    ]