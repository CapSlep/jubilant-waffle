# Generated by Django 4.2.2 on 2023-06-23 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_todo_completedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completedTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='until',
            field=models.DateTimeField(blank=True),
        ),
    ]