# Generated by Django 3.2.16 on 2023-02-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230218_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default=False, max_length=254),
        ),
    ]
