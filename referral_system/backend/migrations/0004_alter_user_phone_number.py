# Generated by Django 4.1.7 on 2023-08-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_user_phon_code_phoncode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(unique=True),
        ),
    ]
