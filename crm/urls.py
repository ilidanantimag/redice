from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include


urlpatterns = [
   url(r'^log/$', views.log, name='log'),
   url(r'^crm_updade/$', views.crm_updade, name='crm_updade'),
   url(r'^crm_orders/$', views.crm_orders, name='crm_orders'),
   url(r'^order_complite/(?P<id>[-\w]+)$', views.order_complite, name='order_complite'),
   url(r'^order_return/(?P<id>[-\w]+)$', views.order_return, name='order_return'),
   url(r'^from_the_courier/(?P<id>[-\w]+)$', views.from_the_courier, name='from_the_courier'),
   url(r'^order_sobran/(?P<id>[-\w]+)$', views.order_sobran, name='order_sobran'),
   url(r'^order_sobran_all/$', views.order_sobran_all, name='order_sobran_all'),
   url(r'^from_the_courier_all/$', views.from_the_courier_all, name='from_the_courier_all'),
   url(r'^order_complite_return/$', views.order_complite_return, name='order_complite_return'),
   url(r'^order_new/$', views.order_new, name='order_new'),
   url(r'^singup/$', views.singup, name='singup'),
   url(r'^check_orders/$', views.check_orders, name='check_orders'),
   url(r'^(?P<pk>\d+)$', views.crm_detail, name='crm-detail'),
   url(r'^(?P<pk>\d+)/(?P<color_product>[-\w]+)$', views.crm_detail, name='crm-detail'),
   url(r'^complite_shop/$', views.complite_shop, name='complite_shop'),
   

  
]

