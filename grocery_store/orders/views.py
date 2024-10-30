from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from orders.models import Orders, UOM, Products, OrderDetails
from datetime import datetime
from django.contrib import messages
# Create your views here.


def index(request):
    orders = Orders.objects.all()
    context = {
        'orders': orders
    }
    return render(request, "products.html", context)


def products(request):
    active_products = Products.objects.filter(is_active=True)
    uom = UOM.objects.all()
    context = {
        'products': active_products,
        'uom': uom
    }
    return render(request, "products.html", context)

def new_orders(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, "new_order.html", context)

def orders(request):
    orders = Orders.objects.all()
    context = {
        'orders': orders
    }
    return render(request, "orders.html", context)

def order_details(request):
    order_details = OrderDetails.objects.all()
    context = {
        'order_details': order_details
    }
    return render(request, "order_details.html", context)


def post_order_details(request):
    if request.method == "POST":
        order_id = int(datetime.now().strftime('%Y%m%d%S'))
        date_time = datetime.now().replace(microsecond=0).strftime('%Y-%m-%d %H:%M:%S')
        customer_name = request.POST.get("customer_name")
        grand_total = request.POST.get("grand_total")
        orders = Orders(order_id=order_id, customer_name=customer_name, total=grand_total, datetime=date_time)
        orders.save()

        row_count = len([key for key in request.POST.keys() if key.startswith("product_")])

        for i in range(row_count):
            product_id = request.POST.get(f"product_{i}")
            quantity = request.POST.get(f"quantity_{i}")
            total = request.POST.get(f"total_{i}")

            product_id_instance = get_object_or_404(Products, pk=product_id)

            products = OrderDetails(order_id=orders, product_id=product_id_instance,
                                    quantity=quantity, total_price=total)
            products.save()

        messages.success(request, "New Order Saved In Database.")
        return redirect("new_order")


def products_save(request):
    if request.method=="POST":
        product_name = request.POST.get("pf_product_name")
        uom_id = request.POST.get("pf_uom")
        ppu = request.POST.get("pf_ppu")
        uom_id_instance = get_object_or_404(UOM, pk=uom_id)
        products = Products(name=product_name, uom_id=uom_id_instance, price_per_unit=ppu)
        products.save()
        messages.success(request, f"Product saved {product_name}")
        return redirect("products")

def edit_product(request):
    if request.method=="POST":
        product_id = request.POST.get("select_product")
        edited_name = request.POST.get("pf_edit_name")
        edited_price = request.POST.get("pf_edit_price")
        products = get_object_or_404(Products, pk=product_id)
        products.name = edited_name
        products.price_per_unit = edited_price
        products.save()
        messages.success(request, f"This product is edited{product_id}{edited_name}{edited_price}")
        return redirect("products")

def delete_product(request):
    if request.method=="POST":
        product_id = request.POST.get("delete_product")
        product = get_object_or_404(Products, pk=product_id)
        product.is_active = False
        product.save()
        messages.warning(request, "success")
        return redirect("products")