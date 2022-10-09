# Generated by Django 4.1.2 on 2022-10-09 18:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShareFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpeg', 'jpg', 'png', 'zip'], message='Only "pdf", "jpeg", "jpg", "png", "zip" are acceptable.')])),
                ('link', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_files', to='sharing_app.filelink')),
            ],
        ),
    ]