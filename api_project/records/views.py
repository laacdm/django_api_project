from rest_framework import viewsets
from .models import Record
from .serializers import RecordSerializer

from django.shortcuts import render
from .models import Record

def home(request):
    records = Record.objects.all()
    return render(request, 'records/home.html', {'records': records})

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
