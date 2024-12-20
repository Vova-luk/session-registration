# Generated by Django 5.1.3 on 2024-11-14 17:17

import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrance', '0006_remove_reg_username_alter_reg_patronymic'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
    ]
