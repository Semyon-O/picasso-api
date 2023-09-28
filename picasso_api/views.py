from rest_framework import generics, status
from .models import File
from .serializers import FileSerializer
from .tasks import make_processed_file
from rest_framework.response import Response

class ListFileView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class UploadNewFile(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        file = request.data.get('file')
        new_file = File.objects.create(file=file)
        make_processed_file.delay(new_file.id)
        ser_result = FileSerializer(new_file)
        return Response(ser_result.data,status=status.HTTP_201_CREATED)
