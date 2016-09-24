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
    url(r'^cart/(?P<post_id>\d+)/$', views.delete_cart_item, name='cart-delete-item'),
    #order
    url(r'^addorder/$', views.add_to_order, name='add-order'),
    url(r'^order/$', views.order, name='order'),
    url(r'^order/(?P<post_id>\d+)/$', views.orderDetail, name='order-detail'),
    # customer
    url(r'^customer/$', views.customer_page, name='customer'),
    url(r'^add_fatturazionecustomer/$', views.add_customer_fatturazione, name='add-fatturazione'),
    url(r'^add_indirizzo_spedizione/$', views.add_customer_indirizzo_spedizione, name='add-indirizzo-spedizione'),
    url(r'^update_fatturazionecustomer/(?P<pk>\d+)/$', views.update_customer_fatturazione, name='update-fatturazione'),
    url(r'^update_indirizzo_spedizione/(?P<pk>\d+)/$', views.update_customer_indirizzo_spedizione, name='update-indirizzo-spedizione'),
    ## cerca
    url(r'^results/$', views.search, name="risultati"),
    #login
    url(r'^logout/$', views.logout_view, name='logout'),
    ## pagine statiche
    url(r'^chi-siamo/$', views.chisiamo, name='chi-siamo'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^servizio-clienti/$', views.servizio_clienti, name='servizio-clienti'),
    url(r'^contact/$', views.contact, name='contact'),
   ]
