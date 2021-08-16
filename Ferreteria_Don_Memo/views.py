from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import RegisterForm
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from productos.models import Product

def index(request):

    products = Product.objects.all().order_by('-id')

    return render(request,'index.html', {
        'mensaje': 'Listado de productos',
        'titulo': 'Productos',
        'products': products,
    })

    return render(request, 'index.html', {
        'mensaje': 'Listado de productos',
        'titulo': 'Productos',
        'products' : [
            {'titulo':'Taladro','precio':2500, 'stock': True},
            {'titulo':'Desarmador','precio':120, 'stock': False},
            {'titulo':'Tornillos 8/8','precio':5, 'stock': True},
            {'titulo':'Compresora Thunder','precio':6500, 'stock':True}
        ]
        })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {} feliz dia :)'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'El usuario y/o contraseña que ha ingresado no existen')

    return render(request, 'usuarios/login.html',{

    })

def logout_view(request):  
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente, hasta pronto :D')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request, 'usuarios/register.html', {
        'form': form
    })