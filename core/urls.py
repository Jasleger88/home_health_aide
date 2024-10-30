# home_health_site/urls.py

from django.contrib import admin
from django.urls import path, include
from core.views import process_payment  # Import the process_payment function

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Ensure 'core.urls' is correct
    path('checkout/', include('core.urls')),  # Check if this is necessary
]
