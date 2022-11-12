from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .helper import get_category_item_names_and_images


def index(request):
    return render(request, 'pages/index.html')

def category(request, category):
    data = get_category_item_names_and_images(category)
    data['category'] = category

    return render(request, 'pages/category.html', data)

def product(request, product_id):
    return HttpResponse(f'this is the product page for {product_id}')

def shopping_cart(request):
    return HttpResponse(f'this is the shopping cart page')

def search(request):
    return HttpResponse(f'this is the search page')
