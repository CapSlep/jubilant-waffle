# Generated by Django 4.2.11 on 2024-04-09 18:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_alter_todo_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="user_id",
            new_name="user",
        ),
    ]
