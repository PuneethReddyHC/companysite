"""
Definition of urls for python_webapp_django.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib import admin
import hello
import hello.views
from django.urls import path, include
# Uncomment the next lines to enable the admin:
from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap


sitemaps = {
    "posts": PostSitemap,
}
urlpatterns = [
    # Examples:
    
    url(r'^admin/', admin.site.urls),
    path('careers/', include('jobsapp.urls'), name="careers-urls"),
    path('blogs/', include('blog.urls'), name="blogs-urls"),
    path('', include('accounts.urls'), name="account-urls"),
    path('api/', include([
        path('', include('jobsapp.api.urls')),
    ])),
    
    path("summernote/", include("django_summernote.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    url(r'^$', hello.views.home, name='home'),
    url(r'^contact$', hello.views.contact, name='contact'),
    url(r'^services$', hello.views.services, name='services'),
    url(r'^portfolio$', hello.views.portfolio, name='portfolio'),
    url(r'^portfolio-single$', hello.views.contact, name='portfolio-single'),
    url(r'^single-blog$', hello.views.contact, name='single-blog'),
    url(r'^about$', hello.views.about, name='about'),
    
    
    
]
