from django.shortcuts import render, get_object_or_404
from .forms import SingUpForm
from catalog.models import ProductInstance,Сategories,Product, Gallery 
from cart.models import Orders, OrdersUs, CompliteOrders
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import CompliteShop
import uuid


@login_required
def log(request,):
    session_key = request.session.session_key
    if request.user.is_staff:
        a=request.user
        products = Product.objects.filter(slug=a)    
        template = 'crm/staff.html'
    context= {'session_key':session_key,
    'a':a,
    'products': products,
    }    
    session_key = request.session.session_key
                                                                                                               
    return render(request, template, context=context)

def singup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
        username = form.cleaned_data.get('username')
        my_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=my_password)
        login(request, user)
        return redirect('index.html')
    else:
        form =SingUpForm()
        return render(request, 'registration/singup.html', {'form':form} )        


def crm_updade(request):
    return_dict = dict()
    print(request.POST)
    data = request.POST
    quantity_id = data.get("quantity_id")
    quantity_product_num =data.get("quantity_product_num")
    c = ProductInstance.objects.get(id=quantity_id)
    c.quantity = quantity_product_num
    c.quantity=int(c.quantity)
    c.save()
    if c.quantity == 0:
        c.delete()
    return JsonResponse(return_dict) 

def crm_orders(request):
    a=request.user
    orders=Orders.objects.filter(product_slug = a)      
    return render(request, 'crm/crm_orders.html', {'orders': orders,'a':a })

def order_complite(request, id):
    a=request.user
    orders=Orders.objects.filter(product_slug = a)
    order_complite = Orders.objects.get(id=id)
    order_complite_save = CompliteOrders.objects.create(user_id =order_complite.user_id, product_slug=order_complite.product_slug,
    product_title=order_complite.product_title,
    product_prace =order_complite.product_prace, product_image =order_complite.product_image,
    product_orders_id = order_complite.product_orders_id, name =order_complite.name, phone =order_complite.phone, 
    adress =order_complite.adress,)
    order_complite.delete()
    return render(request,'crm/crm_orders.html', {'orders': orders,'a':a } ) 
   
def order_return(request, id):
    a=request.user
    orders=Orders.objects.filter(product_slug = a)
    order_complite = Orders.objects.get(id=id)
    c =order_complite.product_orders_id
    b = ProductInstance.objects.get(id=c)
    b.quantity = b.quantity+1
    b.save()
    order_complite.delete()
    return render(request,'crm/crm_orders.html', {'orders': orders,'a':a } )

def from_the_courier(request, id):
    a=request.user
    orders=Orders.objects.filter(product_slug = a)
    from_the_courier = Orders.objects.get(id=id)
    from_the_courier.status = 'k'
    from_the_courier.save()
    return render(request,'crm/crm_orders.html', {'orders': orders,'a':a } )

def order_sobran(request, id):
    a=request.user
    orders=Orders.objects.filter(product_slug = a)
    order_sobran = Orders.objects.get(id=id)
    order_sobran.status = 's'
    order_sobran.save()
    return render(request,'crm/crm_orders.html', {'orders': orders,'a':a } )

def order_sobran_all(request,):
    a=request.user
    orders=Orders.objects.filter(product_slug = a, status='s')
    return render(request,'crm/crm_orders.html', {'orders': orders, 'a':a} )

def from_the_courier_all(request,):
    a=request.user
    orders=Orders.objects.filter(product_slug = a, status='k')
    return render(request,'crm/crm_orders.html', {'orders': orders, 'a':a} )

def order_complite_return(request,):
    a=request.user
    orders=CompliteOrders.objects.filter(product_slug = a,)
    return render(request,'crm/crm_orders.html', {'orders': orders,'a':a } )

def order_new(request):
    a=request.user
    orders=Orders.objects.filter(product_slug = a, status='n')
    return render(request,'crm/crm_orders.html', {'orders': orders, 'a':a } )

    
def check_orders(request):
    print(request.POST)
    data=request.POST
    id_shop = data.get("id_shop")
    count_orders = Orders.objects.filter(product_slug = id_shop).count()
    print(count_orders)
    return_dict = count_orders

    
    return JsonResponse({'return_dict':return_dict}) 

def crm_detail(request, pk, color_product=None):
    if color_product == None:
        color=None
        color_all = []
        categories=Сategories.objects.all()
        product = get_object_or_404(Product, id=pk, available=True)
        product_color = ProductInstance.objects.filter(product=product)[:1]
        product_category = Product.objects.filter(product_subcategories=product.product_subcategories).order_by('?')[:4]
        for i in product_color:
            color = i.color
        gallery = Gallery.objects.filter(product=product, color=color)
        product_color_all = Gallery.objects.filter(product=product,)
        for c in product_color_all:
            i = c.color
            if i not in color_all:
                color_all.append(i)    
        product_size = ProductInstance.objects.filter(product=product, color=color)
        color_image=gallery[:1]                                                                                                               
        return render(request, 'crm/crm_detail.html', {'product': product,'categories': categories, 'gallery':gallery,
         'product_size':product_size, 'color_all': color_all, 'color_image':color_image, 'product_category':product_category })
        
    color_product=color_product
    color_all=[]
    categories=Сategories.objects.all()
    product = get_object_or_404(Product, id=pk, available=True)
    gallery = Gallery.objects.filter(product=product, color=color_product)
    product_color_all = Gallery.objects.filter(product=product,)
    product_category = Product.objects.filter(product_subcategories=product.product_subcategories).order_by('?')[:4]
    for c in product_color_all:
        i = c.color
        if i not in color_all:
            color_all.append(i)         
    product_size = ProductInstance.objects.filter(product=product, color=color_product)
    color_image=gallery[:1]
    print(color_image)    
    return render(request, 'crm/crm_detail.html', {'product': product,'categories': categories, 'gallery':gallery,
         'product_size':product_size, 'color_all': color_all, 'color_image':color_image, 'product_category':product_category })


def complite_shop(request):
    return_dict = dict()
    print(request.POST)
    data = request.POST
    product_title = data.get("product_title")
    product_size_id=data.get("product_size_id")
    product_prace = data.get("product_prace")
    product_image = data.get("product_image")
    product_slug = data.get("product_slug")
    product_quantity = ProductInstance.objects.get(id=product_size_id)
    new_product = CompliteShop.objects.create(product_size_id=product_size_id, product_title=product_title,
    product_image = product_image, product_prace = product_prace, product_slug=product_slug,
    product_quantity=product_quantity.quantity, product_size=product_quantity.size)
    return JsonResponse(return_dict)    


    
