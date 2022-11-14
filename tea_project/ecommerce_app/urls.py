from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:category>/', views.category, name='category'),
    path('product/<int:product_id>', views.product, name='product'),
    path('product/<int:product_id>/add', views.add_to_cart, name='add'),
    path('shopping_cart/', views.shopping_cart, name='cart'),
    path('search/', views.search, name='search'),
]