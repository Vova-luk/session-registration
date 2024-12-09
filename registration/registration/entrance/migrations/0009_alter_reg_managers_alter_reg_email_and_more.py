# Generated by Django 5.1.3 on 2024-11-30 08:54

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrance', '0008_alter_reg_email_alter_reg_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='reg',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='reg',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='reg',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]