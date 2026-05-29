from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('create/', views.create_app, name='create_app'),
=======
    path('create/', views.create_application, name='create_application'),
>>>>>>> 3dc41b8156e7404e074383ad3ee1b8df3b6dc39f
    path('add_review/<int:app_id>/', views.add_review, name='add_review'),
]