from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Zayavka


@login_required
def create_app(request):
    if request.method == 'POST':
        Zayavka.objects.create(
            polzovatel=request.user,
            kurs=request.POST.get('course', ''),
            data_nachala=request.POST.get('start_date', ''),
            oplata=request.POST.get('payment_method', '')
        )
        return redirect('home')
    return render(request, 'applications/create.html')


@login_required
def add_review(request, app_id):
    zayavka = get_object_or_404(Zayavka, id=app_id, polzovatel=request.user)
    if zayavka.status != 'completed':
        return redirect('home')
    if request.method == 'POST':
        zayavka.otzyv = request.POST.get('review', '')
        zayavka.save()
        return redirect('home')
    return render(request, 'applications/add_review.html', {'zayavka': zayavka})