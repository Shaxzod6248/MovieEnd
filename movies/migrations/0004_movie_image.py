# Generated by Django 4.1.4 on 2022-12-19 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
