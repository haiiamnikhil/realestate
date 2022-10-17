from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('home.urls')),
    path('superadmin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('properties/', include('properties.urls')),
    path('auth/', include('authentication.urls')),
    path('user/', include('user.urls')),
    path('notification/', include('notifications.urls')),
]


urlpatterns += static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)