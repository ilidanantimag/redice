import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid

class Сategories(models.Model): 
    categories_title = models.CharField(max_length=200, db_index=True, help_text="Введите категорию товара")
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    def __str__(self):
        return self.categories_title
    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'     

class Subсategories(models.Model):
    subcategories_title = models.CharField(max_length=200, db_index=True, help_text="Введите подкатегорию товара")
    categories = models.ForeignKey('Сategories', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    def get_absolute_url(self):
        return reverse('subcategory', args=[self.slug,])
    def __str__(self):
        return self.subcategories_title    
    class Meta:
        verbose_name = 'Подкатегории'
        verbose_name_plural = 'Подкатегории'             


class Product(models.Model):
    product_title = models.CharField('Название товара', db_index=True, max_length = 200)
    slug = models.SlugField(max_length=200, db_index=True)
    product_brend = models.CharField('Бренд', max_length = 50)
    product_numder = models.CharField('Номер продукта', max_length = 100)
    product_categories = models.ForeignKey('Сategories', on_delete=models.SET_NULL, null=True, related_name='products' ) 
    product_subcategories = models.ForeignKey('Subсategories', on_delete=models.SET_NULL, null=True)
    product_image = models.ImageField(upload_to='images/', null=True, blank=True)
    product_description = models.TextField('Описание товара')
    product_prace = models.FloatField('цена товара')
    product_pub_date = models.DateTimeField('Дата публикации')
    available = models.BooleanField(default=True)
    LOAN_STATUS = (
        ('o', 'недоступен'),
           
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='none', help_text='Статус')
    def __str__(self):
        return self.product_title
    def get_absolute_url(self):
       return reverse('product-detail', args=[str(self.id)])    
    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))
    class Meta:
        ordering = ('product_title',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='image')
    color = models.CharField(max_length=20) 
    def get_absolute_url(self):
       return reverse('galery-detail', args=[str(self.id)]) 

class ProductInstance(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=20) 
    size = models.CharField(max_length=20)
    quantity = models.PositiveSmallIntegerField('Количество')
    def __str__(self):
       return '%s (%s)' % (self.id, self.size) # Поменять!!!!!!!
    class Meta:
        verbose_name = 'Размер и количество'
        verbose_name_plural = 'размер и количество'    


class Comment(models.Model):
    product_comment = models.ForeignKey(Product, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length = 50)
    comment_text = models.CharField('Текст статьи', max_length = 500)
    def __str__(self):
        return self.autgor_name
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'     