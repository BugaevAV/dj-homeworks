# Generated by Django 4.2.4 on 2023-08-18 18:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0002_advertisement_is_draft_alter_advertisement_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='favorit_add',
            field=models.ManyToManyField(null=True, related_name='favorit_add', to=settings.AUTH_USER_MODEL),
        ),
    ]
