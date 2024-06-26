# Generated by Django 4.2.11 on 2024-04-09 17:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_alter_todofolders_folder_title_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="todo",
            options={"ordering": ["-is_completed", "-updated_at", "-created_at"]},
        ),
        migrations.RenameField(
            model_name="todo",
            old_name="completedTime",
            new_name="completed_at",
        ),
        migrations.RenameField(
            model_name="todo",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="todo",
            old_name="completed",
            new_name="is_completed",
        ),
        migrations.RenameField(
            model_name="todo",
            old_name="updated",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="todo",
            old_name="user",
            new_name="user_id",
        ),
    ]
