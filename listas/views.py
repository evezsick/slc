from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout 
from .models import Product, Lista
from .forms import ProductForm, ListaForm

def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	return render(request, "listas/index.html", {
		"listas": Lista.objects.all()
	})

def Lista(request):
    Listas = Product.objects.all()
    return render(request, 'index.html', {'lista': Lista})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        
        else:
            return render(request, "listas/login.html", {
                "message": "Usuário ou senha invalidos!"
            })
    return render(request, "listas/login.html")


def logout_view(request):
    logout(request)
    return render(request, "listas/login.html", {
                "message": "Desconectado"
            })

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'produto': products})


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form})


def update_product(request, id):
    produto = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form, 'produto': produto})


def delete_product(request, id):
    produto = Product.objects.get(id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('list_products')

    return render(request, 'prod-delete-confirm.html', {'produto': produto})

def create_list(request):
    form = ListaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('Lista')

    return render(request, 'lists-form.html', {'form': form})


def update_list(request, id):
    nome = Lista.objects.get(id=id)
    form = ListaForm(request.POST or None, instance=nome)

    if form.is_valid():
        form.save()
        return redirect('Lista')

    return render(request, 'lists-form.html', {'form': form, 'lista': nome})


def delete_list(request, id):
    nome = Product.objects.get(id=id)

    if request.method == 'POST':
        nome.delete()
        return redirect('Lista')

    return render(request, 'list-delete-confirm.html', {'lista': nome})