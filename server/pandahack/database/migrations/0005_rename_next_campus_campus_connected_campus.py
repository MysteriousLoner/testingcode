# Generated by Django 5.0.9 on 2024-09-27 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_alter_campus_campus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campus',
            old_name='next_campus',
            new_name='connected_campus',
        ),
    ]
