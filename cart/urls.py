from django.conf.urls import url
from . import views


urlpatterns = [
  
    url(r'^add/cart_adding/$', views.cart_adding, name='cart_adding'),
    url(r'^cart_detail/$', views.cart_detail, name='cart_detail'),
    url(r'^cart_detail/(?P<product_size_id>[-\w]+)$', views.update, name='update'),
    url(r'^orders/$', views.orders, name='orders'),


]