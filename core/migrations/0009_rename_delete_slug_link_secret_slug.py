# Generated by Django 4.0.4 on 2022-05-21 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_link_delete_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='delete_slug',
            new_name='secret_slug',
        ),
    ]
