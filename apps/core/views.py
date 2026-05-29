from django.shortcuts import render
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from apps.applications.models import Zayavka


@login_required
def home(request):
    zayavki = Zayavka.objects.filter(polzovatel=request.user).order_by('-sozdan')
    return render(request, 'core/home.html', {'zayavki': zayavki})
=======
from apps.applications.models import Application

@login_required
def main_screen(request):
    applications = Application.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'core/main_screen.html', {'applications': applications})
# Create your views here.
>>>>>>> 3dc41b8156e7404e074383ad3ee1b8df3b6dc39f
