# Generated by Django 3.2.16 on 2023-02-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_auto_20230221_2006"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="email",
            field=models.EmailField(default="", max_length=254, unique=True),
        ),
    ]
