# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from product.models import *
from product.forms import *
from sito.models import *
from cart.models import *
from order.models import *
from django.core.mail import send_mail
from filer.models import *
#
#login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect

from django.db.models import Sum
from decimal import *
from decimal import Decimal

from django.core.mail import EmailMultiAlternatives

from django.contrib import messages

import datetime

from sito.helper import *

# Create your views here.


@login_required(login_url="/login/")
def HomePage(request):
    slider_list = Slider.objects.filter(active=True).order_by('id')
    last_list = Product.objects.all().order_by('-pub_date')[:4]
    promo_list = Product.objects.filter(promo=True).filter(slide = True).order_by('-pub_date')[:4]
    offerte_list = Product.objects.filter(promo=True).order_by('-id')[:4]
    product_list = Product.objects.all()[:4]
    season = get_stagione(date(2017, 02, 01), date(2017, 8, 30)) #ottengo la stagione dalla funzione in helper.py
    context = {'slider_list':slider_list,
    			'last_list':last_list,
    			'promo_list':promo_list,
                'product_list':product_list,
                'offerte_list':offerte_list,
               'season':season}
    return render_to_response('index.html', context, context_instance=RequestContext(request))



@login_required(login_url="/login/")
def ProductFilterCategory(request, post_id):
    product_list = Product.objects.filter(category__in=post_id)
    context = {'product_list': product_list}
    return render_to_response('price_list.html', context, context_instance=RequestContext(request))


@login_required(login_url="/login/")
def ProductFilterTag(request, post_id):
    product_list = Product.objects.filter(tags__in=post_id)
    context = {'product_list': product_list}
    return render_to_response('category_list.html', context, context_instance=RequestContext(request))


@login_required(login_url="/login/")
def product_list(request):
    product_list = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'price_list.html', {'product_list': product_list})



@login_required(login_url="/login/")
def ProductFilterView(request, post_id):
    product = Product.objects.get(pk=post_id)
    composition_list = Composition.objects.filter(product_id=product.id)
    a = []
    for co in composition_list:
        a += [co.color_id]
    color_list = Color.objects.filter(id__in=a)
    filer_list = Image.objects.filter(folder_id = product.album)
    lunghezzacinture_list = CintureLunghezza.objects.all()
    tagliascarpe_list = TagliaScarpe.objects.all()
    form = ProductForm()
    context = {'product': product,
                'composition_list':composition_list,
                'color_list':color_list,
    			'filer_list':filer_list,
                'lunghezzacinture_list':lunghezzacinture_list,
                'tagliascarpe_list':tagliascarpe_list,
                'form':form}
    return render_to_response('detail.html', context, context_instance=RequestContext(request))


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/')






## cart
def add_to_cart(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            if post.composition:
                if post.quantity > post.composition.quantity:
                    messages.error(request, 'Quantita superiore al magazzino disponibile')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    post.save()
                    messages.success(request, 'Prodotto Aggiunto al carrello')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    #return redirect('/', pk=post.pk)
            else:
                post.save()
                messages.success(request, 'Prodotto Aggiunto al carrello')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                #return redirect('/', pk=post.pk)
    else:
        form = AddForm()
    return render(request, 'cart-form.html', {'form': form})


def show_cart(request):
    cart_list = CartItem.objects.filter(user_id=request.user.id)
    context = {'cart_list':cart_list}
    return render_to_response('cart.html', context, context_instance=RequestContext(request))




## ORDER
def add_to_order(request):
    if request.method == "POST":
        form = AddOrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            #post.tot_price = CartItem.objects.filter(user_id=request.user.id).aggregate(Sum('price_total'))
            tmp_price_total = CartItem.objects.filter(user_id=request.user.id).aggregate(Sum('price_total')) #estrapolo il campo
            post.tot_price = tmp_price_total['price_total__sum'] #estrapolo il campo e lo sommo
            tmp_tot_discount = CartItem.objects.filter(user_id=request.user.id).aggregate(Sum('price_discount'))
            post.tot_discount = tmp_tot_discount['price_discount__sum']
            tot_price_reserved = CartItem.objects.filter(user_id=request.user.id).aggregate(Sum('price_reserved'))
            post.tot_price_reserved = tot_price_reserved['price_reserved__sum']
            post.save()
            cart_list = CartItem.objects.filter(user_id=request.user.id)
            for cart in cart_list:
                formOrder = AddOrderItemForm(request.POST)
                post_cart = formOrder.save(commit=False)
                post_cart.order = post
                post_cart.product = cart.product
                post_cart.composition = cart.composition
                post_cart.price = cart.price
                post_cart.quantity = cart.quantity
                post_cart.total = cart.price_total
                post_cart.price_discount = cart.price_discount
                post_cart.price_reserved = cart.price_reserved
                post_cart.save()

            cart_list.delete() #cancello carrello dopo ordine

            ### email
            '''
            subject = 'Ordine da dal sito internet'
            #message = form.cleaned_data['messaggio']
            ord_list = Order.objects.get(pk=post.id) 
            message = render_to_string('order_email.html', {'post': ord_list})
            sender = [request.user.email]
            cc_myself = False
            recipients = ['pierangelo1982@gmail.com']
            if cc_myself:
                recipients.append(sender)
            
            send_mail(subject, message, sender, recipients)
            '''
            ord_list = Order.objects.get(pk=post.id) 
            ordine = "ordine id: ordine effettuato da: " + request.user.username
            subject, from_email, to = ordine, request.user.email, 'stefano.solinas.bs@gmail.com'
            text_content = 'This is an important message.'
            html_content = render_to_string('order_email.html', {'post': ord_list})
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
                #return HttpResponseRedirect('/success/') # Redirect after POST

            return redirect('/order', pk=post.pk)
    else:
        form = AddOrderForm()
    return render(request, 'order-form.html', {'form': form})



def delete_cart_item(request, post_id):
    cart = CartItem.objects.get(pk=post_id).delete()
    messages.success(request, 'Prodotto eliminato dal carrello')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


########   ORDER    #########
def order(request):
    order_list = Order.objects.filter(user_id=request.user.id).order_by('-id')
    context = {'order_list':order_list}
    return render_to_response('order.html', context, context_instance=RequestContext(request))


def orderDetail(request, post_id):
    order = Order.objects.get(pk=post_id)
    context = {'order':order}
    return render_to_response('orderdetail.html', context, context_instance=RequestContext(request))








#### static page ######
def chisiamo(request):
    return render_to_response('chi-siamo.html', context_instance=RequestContext(request))

def terms(request):
    return render_to_response('terms.html', context_instance=RequestContext(request))

def privacy(request):
    return render_to_response('privacy.html', context_instance=RequestContext(request))

def servizio_clienti(request):
    return render_to_response('servizio-clienti.html', context_instance=RequestContext(request))

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = 'MESSAGGIO DAL SITO shop.bergeitalia.com'
            #message = form.cleaned_data['messaggio']
            message = render_to_string('contact.txt', {'post': request.POST})
            sender = form.cleaned_data['email']
            cc_myself = False

            recipients = ['stefano.solinas.bs@gmail.com']
            if cc_myself:
                recipients.append(sender)
        
            send_mail(subject, message, sender, recipients)
            messages.success(request, 'Messaggio inviato ti ricontatteremo al piu presto')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Messaggio non inviato')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





###  GLOBALI ###
def CategoryMenuView(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return context

def stagioni(request):
    return season
