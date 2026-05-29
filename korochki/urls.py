<<<<<<< HEAD
=======
"""
URL configuration for korochki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
>>>>>>> 3dc41b8156e7404e074383ad3ee1b8df3b6dc39f
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('users/', include('apps.users.urls')),
    path('apps/', include('apps.applications.urls')),
    path('', include('apps.core.urls')),
]
=======
    path('users/', include('apps.users.urls')), #страница users
    path('applications/', include('apps.applications.urls')), # страница applications
    path('', include('apps.core.urls')), # страница core
]
>>>>>>> 3dc41b8156e7404e074383ad3ee1b8df3b6dc39f
