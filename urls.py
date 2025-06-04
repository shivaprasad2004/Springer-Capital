# urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),  # Include employee app URLs
    path('api/', include('attendance.urls')),  # Include attendance app URLs
]
