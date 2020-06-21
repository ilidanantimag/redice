from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf.urls import url





urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('cart/', include('cart.urls')),
]

urlpatterns += [
     path('catalog/', include('catalog.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

urlpatterns += [
    path('crm/', include('crm.urls')),
]





# Используйте static() чтобы добавить соотношения для статических файлов
# Только на период разработки
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path( 'accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += [
    path('crm/', include('django.contrib.auth.urls')),
]


