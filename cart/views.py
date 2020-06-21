from django.shortcuts import render
from django.views.decorators.http import require_POST
from catalog.models import ProductInstance,Сategories
import uuid
from .models import ProductInCart, Orders, OrdersUs
from django.http import JsonResponse
from django.contrib.sessions.models import Session







def cart_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_title = data.get("product_title")
    product_size_id=data.get("product_size_id")
    product_prace = data.get("product_prace")
    product_image = data.get("product_image")
    product_slug = data.get("product_slug")
    product_quantity = ProductInstance.objects.get(id=product_size_id)
    
    new_product = ProductInCart.objects.create(session_key=session_key, product_size_id=product_size_id, product_title=product_title,
    product_image = product_image, product_prace = product_prace, product_slug=product_slug,
    product_quantity=product_quantity.quantity, product_size=product_quantity.size)
    return JsonResponse(return_dict)

def cart_detail(request,):
    categories = Сategories.objects.all()
    session_key = request.session.session_key
    cart_product = ProductInCart.objects.filter(session_key=session_key,)                                                                                                            
    return render(request, 'cart/detail.html', {'cart_product': cart_product, 'categories':categories})

def update(request,product_size_id):
    categories = Сategories.objects.all()
    session_key = request.session.session_key
    cart_product = ProductInCart.objects.filter(session_key=session_key,)
    delite_product = ProductInCart.objects.filter(session_key=session_key, product_size_id=product_size_id)  
    delite_product.delete()                                                                                                          
    return render(request, 'cart/detail.html', {'cart_product': cart_product, 'categories':categories })

    

def orders(request):
    return_dict = dict()
    print(request.POST)
    data = request.POST
    firstname = data.get("firstname")
    phone = data.get("phone")
    lastname =data.get("lastname")
    adress = data.get("adress") 
    session_key = request.session.session_key
    cart_product = ProductInCart.objects.filter(session_key=session_key,)
    user_orders = OrdersUs.objects.create(name=firstname, phone=phone)
    for b in cart_product:
        orders = Orders.objects.create(user_id=user_orders.id, adress=adress, product_orders_id=b.product_size_id,
         product_slug=b.product_slug, phone =phone, name = firstname, product_title =b.product_title, product_prace=b.product_prace, product_image =b.product_image )

    for i in cart_product:
        c = ProductInstance.objects.get(id=i.product_size_id)
        c.quantity = c.quantity-1
        c.save()
        if c.quantity == 0:
            c.delete()
        b = ProductInCart.objects.filter(product_size_id=i.product_size_id)
        for o in b:
            o.product_quantity = o.product_quantity-1
            o.save()     
    cart_product.delete() 
    return JsonResponse(return_dict)

