# Generated by Django 4.0.4 on 2022-05-20 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_shortener_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='shorten',
            field=models.CharField(blank=True, max_length=16, unique=True),
        ),
    ]
