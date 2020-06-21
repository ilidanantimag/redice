from django.contrib import admin
from .models import Сategories, Subсategories, Product, Comment, ProductInstance, Gallery



#admin.site.register(Сategories)
admin.site.register(Subсategories)
#admin.site.register(Product)
#admin.site.register(ProductInstance)
admin.site.register(Comment)



class ProductInstanceInline(admin.TabularInline):
    model = ProductInstance
    extra = 0

class GalleryInline(admin.StackedInline):
    fk_name = 'product'
    model = Gallery
    extra = 0
class SubсategoriesInstanceInline(admin.TabularInline):
    model = Subсategories
    extra = 0

@admin.register(Сategories)
class СategoriesAdmin(admin.ModelAdmin):
    list_display = ('categories_title', 'slug',)
    inlines = [SubсategoriesInstanceInline]

 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'product_categories','product_image')
    list_filter = ('product_categories',)
    inlines = [ProductInstanceInline, GalleryInline]
    

@admin.register(ProductInstance)
class ProductInstanceAdmin(admin.ModelAdmin):
    ist_display = ('size', 'quantity')
    list_filter = ('size', 'quantity')
