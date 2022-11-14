from .csv_interface import CSV_Interface
import collections, functools, operator

products_interface = CSV_Interface('./ecommerce_app/data/products.csv')
cart_interface = CSV_Interface('./ecommerce_app/data/shopping_cart.csv')

def get_category_item_names_and_images(category):
    data = {}
    product_names_and_images = []
    products = products_interface.all_data

    category_items = [item for item in products for column_value in item.values() if category == column_value]

    for item in category_items:
        temp = []
        for key, value in item.items():
            if key == 'image_url':
                temp.append(value)
            elif key == 'name':
                temp.append(value)
            elif key == 'id':
                temp.append(value)
                
        product_names_and_images.append(temp)

    data['category_items'] = product_names_and_images
    return data

def get_product_by_name(name):
    data = {}
    products = products_interface.all_data

    for item in products:
        for key, value in item.items():
            if key == 'name' and value == name:
                data = item

    return data

def get_product_details(product_id):
    data = {}
    products = products_interface.all_data

    for item in products:
        for key, value in item.items():
            if key == 'id' and value == str(product_id):
                data = item

    return data
   

def add_to_cart_csv(cart):
    cart_interface.append_one_row_to_file(cart)

def get_item_names_and_cost(product_id):
    products = products_interface.all_data

    item_by_id = [item for item in products for k,v in item.items() if k=='id' and v==product_id] 
    item_name_and_cost = {}
    item_name_and_cost['name'] = item_by_id[0]['name']
    item_name_and_cost['cost'] = int(item_by_id[0]['cost'])

    return item_name_and_cost

def translate_cart():
    data = {}
    cart_products = cart_interface.all_data
    cart_details = []
    grand_total = 0
    
    for item in cart_products:
        for key,value in item.items():
            if key == 'id':
                cart_details.append(get_item_names_and_cost(value))
    
    for i in range(len(cart_products)):
        cart_details[i]['id'] = cart_products[i]['id']
        cart_details[i]['qty'] = int(cart_products[i]['qty'])
        cart_details[i]['total_cost'] = int(cart_products[i]['qty']) * int(cart_details[i]['cost'])
        grand_total += cart_details[i]['total_cost']
    
    data['cart'] = cart_details
    data['grand_total'] = grand_total

    return data
    



