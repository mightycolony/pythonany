# Generated by Django 4.1 on 2023-10-25 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app_auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='protfoloo_site',
            new_name='protfolio_site',
        ),
    ]
