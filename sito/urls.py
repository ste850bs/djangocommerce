from django.conf.urls import include, url, patterns
from django.contrib import admin
from sito import views
from sito.views import *
from django.conf import settings
from django.conf.urls.static import static
from sito.forms import LoginForm



urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage, name='home'),
    url(r'^product/(?P<post_id>\d+)/$', views.ProductFilterView, name='detail'),
    url(r'^category/(?P<post_id>\d+)/$', views.ProductFilterCategory, name='categoria'),
    url(r'^tags/(?P<post_id>\d+)/$', views.ProductFilterTag, name='tag-filter'),
    url(r'^product-list$', views.product_list, name='product-list'),
    #cart
    url(r'^add/$', views.add_to_cart, name='add'),
     url(r'^cart/$', views.show_cart, name='show-cart'),
    #login
    url(r'^logout/$', views.logout_view, name='logout'),

   ]