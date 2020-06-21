from django.db import models
import uuid
from django.urls import reverse
from catalog.models import Product, ProductInstance


class ProductInCart(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    session_key = models.CharField(max_length=200,)
    product_slug = models.CharField(max_length=200,)
    product_image = models.ImageField(upload_to='images/', null=True, blank=True)
    product_size_id = models.UUIDField(default=uuid.uuid4,  help_text="Unique ID for this particular book across whole library")
    product_size = models.CharField(max_length=20,)
    product_title = models.CharField(max_length=200,)
    product_prace =  models.FloatField('цена товара')
    product_quantity = models.PositiveSmallIntegerField('Количество')
    def __str__(self):
       return '%s ()' % (self.product_size_id)
    def get_absolute_url(self):
       return reverse('update', args=[str(self.product_size_id)])    

class Orders(models.Model):
   product_slug = models.CharField(max_length=200,)
   user_id = models.CharField(max_length=60)
   product_title = models.CharField(max_length=200,)
   product_prace =  models.FloatField('цена товара')
   product_image = models.ImageField(upload_to='images/', null=True, blank=True)
   product_orders_id = models.UUIDField(default=uuid.uuid4,  help_text="Unique ID for this particular book across whole library")
   name = models.CharField(max_length=200)
   phone = models.CharField(max_length=200)
   adress = models.CharField(max_length=60)
   LOAN_STATUS = (
        ('n', 'Новый'),
        ('k', 'У курьера'),
        ('s', 'Собран'),
      
          
    )
   status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='n', help_text='Статус')
   def __str__(self):
        return self.product_title
   def get_absolute_url(self):
       return reverse('order_complite', args=[str(self.id)] )
       
   def get_absolute_urlw(self):
       return reverse('order_return', args=[str(self.id)] )

   def get_absolute_urlcourier(self):
       return reverse('from_the_courier', args=[str(self.id)] )
   def get_absolute_urlsobran(self):
       return reverse('order_sobran', args=[str(self.id)] )                

class CompliteOrders(models.Model):
   product_slug = models.CharField(max_length=200,)
   user_id = models.CharField(max_length=60)
   product_title = models.CharField(max_length=200,)
   product_prace =  models.FloatField('цена товара')
   product_image = models.ImageField(upload_to='images/', null=True, blank=True)
   product_orders_id = models.UUIDField(default=uuid.uuid4,  help_text="Unique ID for this particular book across whole library")
   name = models.CharField(max_length=200)
   phone = models.CharField(max_length=200)
   adress = models.CharField(max_length=60)
   def __str__(self):
        return self.product_title


class OrdersUs(models.Model):
   name = models.CharField(max_length=200)
   phone = models.CharField(max_length=200)
   def __str__(self):
        return self.name
   
   


  
    
    
    
   
     
