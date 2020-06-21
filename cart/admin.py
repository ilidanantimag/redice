from django.contrib import admin
from .models import ProductInCart, Orders, OrdersUs, CompliteOrders

admin.site.register(OrdersUs)
#admin.site.register(ProductInCart)
#admin.site.register(Orders)
admin.site.register(CompliteOrders)

@admin.register(ProductInCart)
class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'product_title','product_size_id')
    list_filter = ('product_title',)

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('user_id', )




# Register your models here.
