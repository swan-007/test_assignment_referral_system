# Generated by Django 4.1.7 on 2023-08-08 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_alter_alieninvitecode_code_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_code_user', to='backend.alieninvitecode')),
            ],
        ),
    ]
