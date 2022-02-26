from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('editorial/', include('applications.editorial.urls')),
    path('autor/', include('applications.autor.urls')),
    path('libro/', include('applications.libro.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
