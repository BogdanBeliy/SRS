from django.contrib import admin
from django.urls import path, include
from core.views import BaseView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', BaseView.as_view(), name='index'),
    path('profile/', include('account.urls')),
    path('ads/', include('ads.urls')),
    path('admin/', admin.site.urls),
    path('silk/', include('silk.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

