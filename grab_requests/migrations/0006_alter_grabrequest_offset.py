# Generated by Django 4.2.1 on 2023-07-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grab_requests', '0005_alter_grabrequest_icon_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grabrequest',
            name='offset',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
