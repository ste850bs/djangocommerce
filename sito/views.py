from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from product.models import *
from sito.models import *
from django.core.mail import send_mail
from filer.models import *




# Create your views here.
def HomePage(request):
    slider_list = Slider.objects.filter(active=True).order_by('id')
    last_list = Product.objects.all().order_by('-pub_date')[:4]
    promo_list = Product.objects.filter(promo=True).order_by('-pub_date')[:4]
    offerte_list = Product.objects.filter(promo=True).order_by('-id')
    product_list = Product.objects.all()[:4]
    category_list = Category.objects.filter(show=True).order_by('id')
    abbigliamento_list = Product.objects.filter(category__in = '7').order_by('-id')[:4]
    context = {'slider_list':slider_list,
    			'last_list':last_list,
    			'promo_list':promo_list,
                'product_list':product_list,
                'offerte_list':offerte_list,
                'category_list':category_list,
                'abbigliamento_list':abbigliamento_list}
    return render_to_response('index.html', context, context_instance=RequestContext(request))



def ProductCategoryView(request, post_id):
    product_list = Product.objects.filter(category__in = post_id)
    category = Category.objects.get(pk=post_id)
    context = {'product_list': product_list,
                'category':category}
    return render_to_response('prodotti.html', context, context_instance=RequestContext(request))



def ProductFilterView(request, post_id):
    product = Product.objects.get(pk=post_id)
    filer_list = Image.objects.filter(folder_id = product.album)
    context = {'product': product,
    			'filer_list':filer_list}
    return render_to_response('detail.html', context, context_instance=RequestContext(request))



###  GLOBALI ###
def CategoryMenuView(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return context
