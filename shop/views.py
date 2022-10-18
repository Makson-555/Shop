from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Category, Product
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    #search
    search_query = request.GET.get('search','')
    if search_query:
        products = Product.objects.filter(name__icontains = search_query)
    else:
        categories = Category.objects.all()

    return render(request,'shop/product/list.html',{'category': category,'categories': categories,'products': products})

def product_detail(request, id, slug):
    a = Product.objects.get(id=id)
    product = get_object_or_404(Product,id=id,slug=slug,available=True)

    return render(request,'shop/product/detail.html',{'product': product,})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)

    return render(request, 'shop/product/detail.html', {'product': product,})
