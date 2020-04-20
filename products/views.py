from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {
        'products': products
    })


@login_required
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:index')
        else:
            return render(request, 'form.html', {
                'form': form
            })
    else:
        form = ProductForm()
        return render(request, 'form.html', {
            'form': form
        })


@login_required
def update(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:index')
        else:
            return render(request, 'form.html', {
                'form': form,
                'product': product.name
            })
    else:
        form = ProductForm(instance=product)
        return render(request, 'form.html', {
            'form': form,
            'product': product.name
        })


@login_required
def delete(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product.delete()

    return redirect('products:index')
