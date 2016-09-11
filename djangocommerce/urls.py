"""djangocommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from sito import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage, name='home'),
    url(r'^product/(?P<post_id>\d+)/$', views.ProductFilterView, name='detail'),
    url(r'^category/(?P<post_id>\d+)/$', views.ProductFilterCategory, name='categoria'),
    url(r'^tags/(?P<post_id>\d+)/$', views.ProductFilterTag, name='tag-filter'),
    url(r'^product-list$', views.product_list, name='product-list'),
    #carton
    url(r'^add/$', views.add, name='shopping-cart-add'),
    #url(r'^remove/$', views.remove, name='shopping-cart-remove'),
    url(r'^show/$', views.show, name='shopping-cart-show'),
    #admin
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)), # admin site
]

if settings.DEBUG:  
        urlpatterns += patterns('',  
                                #REMOVE IT in production phase  
                                (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
                                {'document_root': settings.MEDIA_ROOT})
          )
