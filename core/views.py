# core/views.py
from rest_framework import viewsets
from .models import Service, AboutMe, Contact
from .serializers import ServiceSerializer, AboutMeSerializer, ContactSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Health Aide Website!")

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class AboutMeViewSet(viewsets.ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
