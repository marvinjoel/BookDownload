from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('apps.bookapp.urls')),
    path('', include('apps.login.urls')),
    path('social-auth/', include('social_django.urls', namespace='social'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
