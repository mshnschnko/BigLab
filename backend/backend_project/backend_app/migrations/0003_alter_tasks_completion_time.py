# Generated by Django 4.1.2 on 2022-12-24 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0002_alter_tasks_completion_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='completion_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
