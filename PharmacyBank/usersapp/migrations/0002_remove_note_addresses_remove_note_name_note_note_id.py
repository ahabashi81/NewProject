# Generated by Django 4.0.6 on 2022-07-30 16:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='Addresses',
        ),
        migrations.RemoveField(
            model_name='note',
            name='name',
        ),
        migrations.AddField(
            model_name='note',
            name='note_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]