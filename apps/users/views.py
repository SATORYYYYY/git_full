from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
<<<<<<< HEAD
from .models import User


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        full_name = request.POST.get('full_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()

        if User.objects.filter(username=username).exists():
=======
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']

        if CustomUser.objects.filter(username=username).exists():
>>>>>>> 3dc41b8156e7404e074383ad3ee1b8df3b6dc39f
            return render(request, 'users/register.html', {'error': 'Логин уже занят'})
        if len(password) < 8:
            return render(request, 'users/register.html', {'error': 'Пароль должен быть не менее 8 символов'})

<<<<<<< HEAD
        User.objects.create_user(
=======
        user = CustomUser.objects.create_user(
>>>>>>> 3dc41b8156e7404e074383ad3ee1b8df3b6dc39f
            username=username,
            password=password,
            full_name=full_name,
            phone=phone,
            email=email
        )
<<<<<<< HEAD
        return redirect('login')
    return render(request, 'users/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
=======
        return redirect('login')  
    return render(request, 'users/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
>>>>>>> 3dc41b8156e7404e074383ad3ee1b8df3b6dc39f
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            return redirect('/')
<<<<<<< HEAD
        return render(request, 'users/login.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
=======
        else:
            return render(request, 'users/login.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
# Create your views here.
>>>>>>> 3dc41b8156e7404e074383ad3ee1b8df3b6dc39f
