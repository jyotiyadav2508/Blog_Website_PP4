# Generated by Django 3.2.16 on 2023-02-14 11:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_auto_20230210_1223"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="known_for",
        ),
        migrations.RemoveField(
            model_name="post",
            name="stars",
        ),
    ]
