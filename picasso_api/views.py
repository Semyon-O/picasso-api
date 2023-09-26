from django.http import HttpResponse
from rest_framework import generics
from .models import File
from .serializers import FileSerializer
from .tasks import make_processed_file


class ListFileView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class UploadNewFile(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        file = request.data.get('file')
        new_file = File.objects.create(file=file)
        make_processed_file(new_file)
        return HttpResponse("OK")