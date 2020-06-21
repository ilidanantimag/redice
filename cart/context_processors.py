from .models import ProductInCart

def getting_cart_info(request):

    session_key = request.session.session_key
   

    products_in_cart = ProductInCart.objects.filter(session_key=session_key, )


    return locals()