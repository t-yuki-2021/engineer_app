# Generated by Django 3.1.5 on 2021-02-14 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0002_language_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='introduction',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
