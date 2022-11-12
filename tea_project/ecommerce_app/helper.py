from .csv_interface import CSV_Interface

def get_category_item_names_and_images(category):
    data = {}
    product_names_and_images = []

    products_interface = CSV_Interface('./ecommerce_app/data/products.csv')
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

get_category_item_names_and_images('tea')