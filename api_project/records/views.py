from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Record
from .serializers import RecordSerializer

from django.core.paginator import Paginator
from django.shortcuts import render

def home(request):
    # Define a custom sorting order for the 'type_of_document' field
    type_order = {'Diploma': 1, 'Specialization': 2, 'Certification': 3}

    # Fetch and sort records
    records = Record.objects.all()
    sorted_records = sorted(records, key=lambda r: (type_order.get(r.type_of_document, 4), -r.date.toordinal()))

    # Apply pagination to sorted records
    paginator = Paginator(sorted_records, 10)  # ✅ Show 10 records per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # ✅ Pass `page_obj` to template
    return render(request, 'records/home.html', {'page_obj': page_obj})

class RecordViewSet(viewsets.ModelViewSet):
    """API endpoint that allows authenticated users to view records."""
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    authentication_classes = [TokenAuthentication]  # Explicitly set token authentication
    permission_classes = [IsAuthenticated]  # Require authentication
