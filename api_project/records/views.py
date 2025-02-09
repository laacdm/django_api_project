from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Record
from .serializers import RecordSerializer

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token

# ✅ Home View with Pagination and Sorting
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


# ✅ User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


# ✅ User Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # ✅ Redirect to home after login
    else:
        form = AuthenticationForm()

    return render(request, 'records/login.html', {'form': form})  # ✅ Use correct template path


# ✅ User Logout View
def user_logout(request):
    logout(request)
    return redirect('login')


def about(request):
    return render(request, 'records/about.html')


# ✅ View to Get API Key (Only for Logged-In Users)
@login_required
def get_api_key(request):
    token, created = Token.objects.get_or_create(user=request.user)
    return render(request, 'api_key.html', {'api_key': token.key})


# ✅ API Viewset (No Changes)
class RecordViewSet(viewsets.ModelViewSet):
    """API endpoint that allows authenticated users to view records."""
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    authentication_classes = [TokenAuthentication]  # Explicitly set token authentication
    permission_classes = [IsAuthenticated]  # Require authentication