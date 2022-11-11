from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'pages/index.html')

def category(request, category_id):
    return HttpResponse(f'this is the category page for {category_id}')

def product(request, product_id):
    return HttpResponse(f'this is the product page for {product_id}')

def shopping_cart(request):
    return HttpResponse(f'this is the shopping cart page')

def search(request):
    return HttpResponse(f'this is the search page')
