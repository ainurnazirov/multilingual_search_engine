# Generated by Django 3.2.2 on 2021-05-09 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='query',
            new_name='q',
        ),
    ]
