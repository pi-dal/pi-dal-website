"""dal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include ,re_path
from django.views.generic.base import RedirectView
from django.views.static import serve
from .settings.common import MEDIA_ROOT
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('index.urls')),
    path('tutorial/', include('tutorial.urls')),
    path(r'mdeditor/', include('mdeditor.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path(r'', include('social_django.urls', namespace='social')),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='https://cdn.jsdelivr.net/gh/pi-dal/cdn@1.0/pi-dal.png')),
    path('password-reset/', include('password_reset.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)