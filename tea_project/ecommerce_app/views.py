from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .helper import *
import requests as HTTP_Client 
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
import os


def index(request):
    return render(request, 'pages/index.html')

def category(request, category):
    data = get_category_item_names_and_images(category)
    data['category'] = category

    return render(request, 'pages/category.html', data)

def product(request, product_id):
    data = get_product_details(product_id)

    return render(request, 'pages/product.html', data)

def add_to_cart(request, product_id):
    cart_entry = {'id': product_id}
    quantity = int(request.POST['qty'])
    cart_entry['qty'] = quantity

    add_to_cart_csv(cart_entry)

    return HttpResponseRedirect(f"/chachi/product/{product_id}")

def shopping_cart(request):
    data = translate_cart()
    print(data)
    
    return render(request, 'pages/shopping_cart.html', data)

def search(request):
    load_dotenv()
    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])

    try:
        data = {}
        search_term = request.GET['name']
        data = get_product_by_name(search_term.lower())
        print(search_term)
    
        if data == {}:
            data = {}
            response = HTTP_Client.get(f'https://api.thenounproject.com/icon/{search_term}', auth=auth)
            response_json = response.json()

            data['error_img'] = response_json['icon']['attribution_preview_url']
            data['error_message'] = "Item out of stock or not carried"
    except ValueError:
        return HttpResponseRedirect('/chachi')
    except KeyError:
        if data == {}:
            data = {}
            response = HTTP_Client.get(f'https://api.thenounproject.com/icon/{search_term}', auth=auth)
            response_json = response.json()

            data['error_img'] = response_json['icon']['icon_url']
            data['error_message'] = "Item out of stock or not carried"


    
    return render(request, 'pages/search.html', data)
