# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, AboutMeViewSet, ContactViewSet, home

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'about', AboutMeViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', home),  # Home page at the root
    path('api/', include(router.urls)),  # API routes prefixed with 'api/'
]
