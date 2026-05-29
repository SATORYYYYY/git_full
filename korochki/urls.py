from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('apps/', include('apps.applications.urls')),
    path('', include('apps.core.urls')),
]
