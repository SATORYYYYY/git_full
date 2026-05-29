from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.applications.models import Zayavka


@login_required
def home(request):
    zayavki = Zayavka.objects.filter(polzovatel=request.user).order_by('-sozdan')
    return render(request, 'core/home.html', {'zayavki': zayavki})
