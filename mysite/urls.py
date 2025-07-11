# mysite/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Your app's URLs
]

# ✅ Serve media files even when DEBUG = False
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
