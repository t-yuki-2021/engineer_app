# Generated by Django 3.1.5 on 2021-02-12 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('engineer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_start_at', models.DateField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_language', to='engineer.language')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
