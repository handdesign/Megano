# Generated by Django 4.2.2 on 2023-07-25 14:09

from django.db import migrations, models
import user_auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatars/default.png', upload_to=user_auth.models.avatar_directory_path),
        ),
    ]
