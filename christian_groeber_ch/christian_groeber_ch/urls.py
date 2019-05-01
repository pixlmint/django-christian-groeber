"""christian_groeber_ch URL Configuration

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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import TechnologySitemap, ElementSitemap, TypeSitemap
from django.urls import path, include

from . import settings


sitemaps = {
    'types': TypeSitemap,
    'elements': ElementSitemap,
    'technologies': TechnologySitemap
}

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('website.urls')),
    url('portfolio/', include('portfolio.urls'), name='portfolio'),
    url('contact/', include('contact.urls'), name='url'),
    url('hire-me/', include('hire_me.urls'), name='hire-me'),
    url(r'^froala_editor/', include('froala_editor.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
