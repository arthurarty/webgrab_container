# Generated by Django 4.2.1 on 2023-06-12 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grab_requests', '0006_alter_grabrequest_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grabrequest',
            old_name='site_name',
            new_name='channel_name',
        ),
    ]
