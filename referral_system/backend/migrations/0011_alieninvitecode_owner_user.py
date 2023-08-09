# Generated by Django 4.1.7 on 2023-08-08 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_rename_code_alieninvitecode_alien_invite_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='alieninvitecode',
            name='owner_user',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, related_name='owner_code', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
