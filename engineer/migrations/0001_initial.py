# Generated by Django 3.1.5 on 2021-02-12 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyMemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=30)),
                ('memo', models.TextField(max_length=140)),
                ('time', models.IntegerField(default=30)),
                ('is_public', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_memo_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
