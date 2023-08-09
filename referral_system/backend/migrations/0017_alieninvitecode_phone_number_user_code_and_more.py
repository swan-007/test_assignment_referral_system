# Generated by Django 4.1.7 on 2023-08-08 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_alter_alieninvitecode_code_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='alieninvitecode',
            name='phone_number_user_code',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='alieninvitecode',
            name='code_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alien_invite_code', to=settings.AUTH_USER_MODEL),
        ),
    ]
