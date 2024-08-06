from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Produto

#home
def home(request):
    return render(request, 'produtos/home.html')

# Create your views here.
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:product_list')
    else:
        form = ProductForm()
    
    return render(request, 'produtos/add_product.html', {'form' : form})

def product_list(request):
    products = Produto.objects.all()
    return render(request, 'produtos/product_list.html', {'products': products})



