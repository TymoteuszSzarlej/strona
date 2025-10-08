# RavaDev/urls.py - POPRAWNIE
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main.urls')),
    path('about/', include('About.urls')),
    path('blog/', include('Blog.urls')),
    path('contact/', include('Contact.urls')),
    path('projects/', include('Projects.urls')),
    path('services/', include('Services.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)