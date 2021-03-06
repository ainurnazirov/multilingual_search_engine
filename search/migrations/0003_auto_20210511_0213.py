# Generated by Django 3.2.2 on 2021-05-10 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_rename_query_query_q'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='q',
        ),
        migrations.AddField(
            model_name='query',
            name='n_result',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='n_result_t',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='query',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='query_t',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='search_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
