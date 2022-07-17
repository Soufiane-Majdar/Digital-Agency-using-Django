from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('contact/', include('Contact.urls')),
    path('dashboard/', include('Dashboard.urls')),
    path('service/', include('Service.urls')),
    path('project/', include('Project.urls')),
    path('user/', include('User.urls')),
]


# Serving the media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()