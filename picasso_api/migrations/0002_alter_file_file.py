# Generated by Django 4.2.5 on 2023-09-27 22:00

from django.db import migrations, models
import picasso_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('picasso_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=picasso_api.models.file_id_directory),
        ),
    ]
