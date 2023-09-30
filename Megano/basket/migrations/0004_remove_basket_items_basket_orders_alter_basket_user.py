# Generated by Django 4.2.2 on 2023-07-28 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basket', '0003_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='items',
        ),
        migrations.AddField(
            model_name='basket',
            name='orders',
            field=models.ManyToManyField(blank=True, to='basket.order'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
