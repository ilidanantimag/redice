from django.db import models
import uuid

class CompliteShop(models.Model):
    product_slug = models.CharField(max_length=200,)
    product_image = models.ImageField(upload_to='images/', null=True, blank=True)
    product_size_id = models.UUIDField(default=uuid.uuid4,  help_text="Unique ID for this particular book across whole library")
    product_size = models.CharField(max_length=20,)
    product_title = models.CharField(max_length=200,)
    product_prace =  models.FloatField('цена товара')
    product_quantity = models.PositiveSmallIntegerField('Количество')
    def __str__(self):
       return '%s ()' % (self.product_size_id)
 
