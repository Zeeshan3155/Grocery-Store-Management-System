"""
URL configuration for grocery_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from orders import views

urlpatterns = [
    path("", views.orders, name="home"),
    path("products/", views.products, name="products"),
    path("new-order/", views.new_orders, name="new_order"),
    path("order-details/", views.order_details, name="order_details"),
    path("save-table/", views.post_order_details, name="save_table_data"),
    path("product-save-form/", views.products_save, name="product_save"),
    path("edit-product/", views.edit_product, name="edit_product"),
    path("delete-product/", views.delete_product, name='delete_product')
]
