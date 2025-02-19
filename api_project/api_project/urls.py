"""
URL configuration for api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from records.views import RecordViewSet, home, about, register, user_login, user_logout, get_api_key
from recognitions.views import RecognitionViewSet

router = DefaultRouter()
router.register(r'records', RecordViewSet, basename='record')
router.register(r'recognitions', RecognitionViewSet, basename='recognition')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Register API routes
    path('recognitions/', include('recognitions.urls')),  # ✅ Include recognitions app URLs
    path('', home, name='home'),
    path('about/', about, name='about'),  # ✅ Add About page URL
    path('register/', register, name='register'),
    path('login/', user_login, name='login'), # ✅ Add login page
    path('logout/', user_logout, name='logout'),
    path('get-api-key/', get_api_key, name='get_api_key'), # ✅ API Key Page
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)