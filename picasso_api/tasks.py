from time import sleep
from celery import shared_task
from .models import File


@shared_task()
def make_processed_file(file_id):

    file_to_proceed: File = File.objects.get(id=file_id)
    try:
        with open(f"media/{file_to_proceed.file}", "a") as file:
            file.write("\nОбработано")
        file_to_proceed.processed = True
        file_to_proceed.save()
    except FileNotFoundError:
        return FileNotFoundError
