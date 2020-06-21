from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^product/(?P<category_slug>[-\w]+)/$',views.category_list, name='product_list_by_category'),
    url(r'^product/(?P<subcategory_slug>[-\w]+)$',views.subcategory_list, name='subcategory'),
    url(r'^(?P<pk>\d+)$', views.product_detail, name='product-detail'),
    url(r'^(?P<pk>\d+)/(?P<color_product>[-\w]+)$', views.product_detail, name='product-detail'),
]

