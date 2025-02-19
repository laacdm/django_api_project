from django.urls import path
# from rest_framework.routers import DefaultRouter
from .views import recognitions_page

# router = DefaultRouter()
# router.register(r'recognitions', RecognitionViewSet, basename='recognition')

urlpatterns = [
    path('', recognitions_page, name='recognitions_page'),  # ✅ Web page for recognitions
]