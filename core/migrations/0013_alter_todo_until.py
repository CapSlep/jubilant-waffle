# Generated by Django 5.0.4 on 2024-04-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0012_todofolders_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="until",
            field=models.DateField(blank=True, null=True),
        ),
    ]
