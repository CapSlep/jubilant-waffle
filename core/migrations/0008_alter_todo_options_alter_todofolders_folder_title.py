# Generated by Django 4.2.2 on 2023-06-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_todo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-completed', '-updated', '-created']},
        ),
        migrations.AlterField(
            model_name='todofolders',
            name='folder_title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
