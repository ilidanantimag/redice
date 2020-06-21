from django.shortcuts import render, get_object_or_404
from .models import Сategories, Subсategories, Product, Comment, ProductInstance, Gallery 
from django.views import generic
from django.http import JsonResponse

def index(request):
    products=Product.objects.all().exclude(productinstance=None).order_by("-product_pub_date")[:12]
    product_one=products[0:4]
    product_two=products[4:8]
    product_three=products[8:12]
    categories=Сategories.objects.all()
    subсategories=Subсategories.objects.all()
    num_visit=request.session.get('num_visit', 0)
    request.session['num_visit'] = num_visit+1 
    session_key = request.session.session_key
    print(request.session.session_key)
    return render(
        request,
        'index.html',
        context={'products':products, 'num_visit':num_visit, 'categories': categories, 'subсategories':subсategories, 
        'product_two':product_two,
        'product_one':product_one,
        'product_three':product_three,
        'num_visit':num_visit},
    )


def category_list(request, category_slug=None,):
    subcategories = Subсategories.objects.all()
    categories = Сategories.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = Сategories.objects.get(slug=category_slug)
        subcategories = Subсategories.objects.filter(categories=category)
        products = Product.objects.filter(product_categories=category,).exclude(productinstance=None).order_by("-product_pub_date")[:15]   
        return render(request,
                'catalog/product_list.html',
                context= {'category': category,
                'categories': categories,
                'products': products,
                'subcategories':subcategories,
                })

def subcategory_list(request, subcategory_slug=None):
    categories = Сategories.objects.all()
    products = Product.objects.filter(available=True)
    if subcategory_slug:
        subcategory = Subсategories.objects.get(slug=subcategory_slug)
        category = subcategory.categories
        subcategories = Subсategories.objects.filter(categories=category)
        products = Product.objects.filter(product_subcategories=subcategory, product_categories=category ).order_by("-product_pub_date")    
        return render(request,
                'catalog/product_list.html',
                context= {'category': category,
                'categories': categories,
                'products': products,
                'subcategories':subcategories,
                })
            
from cart.forms import CartAddProductForm
    
def product_detail(request, pk, color_product=None):
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
        return render(request, 'catalog/product_detail.html', {'product': product,'categories': categories, 'gallery':gallery,
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
    return render(request, 'catalog/product_detail.html', {'product': product,'categories': categories, 'gallery':gallery,
         'product_size':product_size, 'color_all': color_all, 'color_image':color_image, 'product_category':product_category })

    
    
    




