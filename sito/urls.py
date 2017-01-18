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
    url(r'^category/(?P<post_id>\d+)/prezzo/$', views.product_category_list, name='categoria-prezzo'),
    url(r'^tags/(?P<post_id>\d+)/$', views.ProductFilterTag, name='tag-filter'),
    url(r'^product-list$', views.product_list, name='product-list'),
    url(r'^pronta-consegna/$', views.ProductPronta, name='pronta-consegna'),
    url(r'^category/(?P<post_id>\d+)/pronta-consegna/$', views.ProductProntaCategory, name='categoria-pronta-consegna'),
    url(r'^consegna-40-gg/$', views.ProductQuaranta, name='consegna-40gg'),
    url(r'^category/(?P<post_id>\d+)/consegna-40gg/$', views.ProductQuarantaCategory, name='categoria-40gg'),
    url(r'^category/(?P<post_id>\d+)/cdalla-A-alla-Z/$', views.ProductCategoryAtoZ, name='categoria-a-z'),
    url(r'^category/(?P<post_id>\d+)/cdalla-Z-alla-A/$', views.ProductCategoryZtoA, name='categoria-z-a'),
    #estate
    url(r'^category-estate/(?P<post_id>\d+)/$', views.ProductEstateCategory, name='categoria-estate'),
    url(r'^estate/$', views.ProductEstate, name='estate'),
    url(r'^category-estate/(?P<post_id>\d+)/prezzo/$', views.product_estate_price, name='categoria-estate-prezzo'),
    url(r'^category-estate-A-to-Z/(?P<post_id>\d+)/$', views.ProductEstateCategoryAtoZ, name='categoria-estate-a-z'),
    url(r'^category-estate-Z-to-A/(?P<post_id>\d+)/$', views.ProductEstateCategoryZtoA, name='categoria-estate-z-a'),
    #promo
    url(r'^promo/$', views.PromoProduct, name='promo'),
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
    url(r'^codice/$', views.search_for_code, name="risultati-codice"),
    #login
    url(r'^logout/$', views.logout_view, name='logout'),
    ## pagine statiche
    url(r'^chi-siamo/$', views.chisiamo, name='chi-siamo'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^servizio-clienti/$', views.servizio_clienti, name='servizio-clienti'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^chart/$', views.charts, name='chart'),
    url(r'^maps/$', views.customer_map, name='customer-map'),
    url(r'^language/(?P<language>[a-z\-]+)/$', views.language),
   ]
