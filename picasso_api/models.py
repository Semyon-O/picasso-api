from django.db import models
from datetime import datetime


def file_id_directory(instance, filename):
    return f"file{str(hash(datetime.now()))}/{filename}"


class File(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to=file_id_directory)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)