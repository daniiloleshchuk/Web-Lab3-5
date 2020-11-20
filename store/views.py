from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


def index(request, **kwargs):
    search_query = kwargs.get('search_query')
    print("SEARCH QUERY", search_query)
    if search_query is not None:
        try:
            products = Product.objects.filter(name__icontains=str(search_query))
        except:
            products = []
    else:
        products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/index.html', context)


def create_page(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('index')
            except:
                pass
    else:
        form = ProductForm()

    context = {'form': form}

    return render(request, 'store/create_page.html', context)


def edit_page(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(initial={'name': product.name, 'description': product.description,
                                'price': product.price, 'image': product.image})
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('index')
            except:
                pass
    context = {'form': form}
    return render(request, 'store/edit_page.html', context)


def delete(request, id):
    product = Product.objects.get(id=id)

    try:
        product.delete()
    except:
        pass

    return redirect('index')
