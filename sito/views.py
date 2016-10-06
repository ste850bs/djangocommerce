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

from django.db.models import Count


from django.core.mail import EmailMultiAlternatives

from django.contrib import messages

import datetime

from django.db.models import Q

from sito.helper import *


# Create your views here.


@login_required(login_url="/login/")
def HomePage(request):
    slider_list = Slider.objects.filter(active=True).order_by('id')
    last_list = Product.objects.filter(active=True).order_by('-pub_date')[:4]
    promo_list = Product.objects.filter(promo=True).filter(slide = True).filter(active=True).order_by('?')[:4]
    offerte_list = Product.objects.filter(active=True).filter(promo=True).order_by('?')[:4]
    top_seller = Product.objects.filter(top_seller=True).order_by('?')[:4]
    product_list = Product.objects.all()[:4]
    season = get_stagione(date(2017, 02, 01), date(2017, 8, 30)) #ottengo la stagione dalla funzione in helper.py
    context = {'slider_list':slider_list,
    			'last_list':last_list,
    			'promo_list':promo_list,
                'product_list':product_list,
                'offerte_list':offerte_list,
                'top_seller':top_seller,
               'season':season}
    return render_to_response('index.html', context, context_instance=RequestContext(request))



@login_required(login_url="/login/")
def ProductFilterCategory(request, post_id):
    product_list = Product.objects.filter(active=True).filter(category__in=post_id)
    context = {'product_list': product_list}
    return render_to_response('price_list.html', context, context_instance=RequestContext(request))



@login_required(login_url="/login/")
def ProductQuaranta(request):
    product_list = Product.objects.filter(active=True).filter(delivery=True)
    context = {'product_list': product_list}
    return render_to_response('price_list.html', context, context_instance=RequestContext(request))



@login_required(login_url="/login/")
def ProductPronta(request):
    product_list = Product.objects.filter(active=True).filter(prompt_delivery=True)
    context = {'product_list': product_list}
    return render_to_response('price_list.html', context, context_instance=RequestContext(request))



@login_required(login_url="/login/")
def ProductEstate(request):
    product_list = Product.objects.filter(active=True).filter(summer=True).filter(prompt_delivery=False)
    context = {'product_list': product_list}
    return render_to_response('price_list.html', context, context_instance=RequestContext(request))



@login_required(login_url="/login/")
def ProductFilterTag(request, post_id):
    product_list = Product.objects.filter(active=True).filter(tags__in=post_id)
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
    comp = Composition.objects.filter(product_id=product.id).values('color_id')
    color_list = Color.objects.filter(id__in=comp)
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
                'comp':comp,
                'form':form}
    return render_to_response('detail.html', context, context_instance=RequestContext(request))


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/')






## cart
## cart
def add_to_cart(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            # controllo se è composizione, poi controllo se composizione già presente, e nel caso aggiorno, sempre che nuova quantità non superi magazzino
            if post.composition:
                if CartItem.objects.filter(user_id=request.user.id).filter(composition_id = post.composition):
                    existing_cart = CartItem.objects.filter(user_id=request.user.id).get(composition_id = post.composition)
                    if post.composition.quantity < (existing_cart.quantity + post.quantity):
                        messages.error(request, 'Prodotto già presente nel carrello, aggiungendo questa quantità si supera la disponibilità in magazzino')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    else:
                        existing_cart.quantity += post.quantity
                        existing_cart.save() 
                        messages.success(request, 'Prodotto già presente, abbiamo aggiornato la quantità')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    if post.quantity > post.composition.quantity:
                        messages.error(request, 'Quantita superiore al magazzino disponibile')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    else:
                        post.save()
                        messages.success(request, 'Prodotto Aggiunto al carrello')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                        #return redirect('/', pk=post.pk)
            else:
                ## cpntrollare se è doppio e poi salvare... controolare che non ci sian composizioni
                ## if cinture
                if post.cintureLunghezza:
                    if CartItem.objects.filter(user_id = request.user.id).filter(composition_id=None).filter(product_id=post.product).filter(color_id=post.color).filter(cintureLunghezza_id=post.cintureLunghezza):
                        ex_cart = CartItem.objects.filter(user_id = request.user.id).filter(composition_id=None).filter(color_id=post.color).filter(cintureLunghezza_id=post.cintureLunghezza).get(product_id=post.product)
                        ex_cart.quantity += post.quantity
                        ex_cart.save()
                        messages.success(request, 'cintura/colore/lunghezza già presente, abbiamo aggiornato la quantità')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
                    else:
                        post.save()
                        messages.success(request, 'Prodotto Aggiunto al carrello')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                ## elif scarpe
                elif post.scarpemisura:
                    if CartItem.objects.filter(user_id = request.user.id).filter(composition_id=None).filter(product_id=post.product).filter(color_id=post.color).filter(scarpemisura_id=post.scarpemisura):
                        ex_cart = CartItem.objects.filter(user_id = request.user.id).filter(composition_id=None).filter(color_id=post.color).filter(scarpemisura_id=post.scarpemisura).get(product_id=post.product)
                        ex_cart.quantity += post.quantity
                        ex_cart.save()
                        messages.success(request, 'scarpa/colore/misura già presente, abbiamo aggiornato la quantità')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
                    else:
                        post.save()
                        messages.success(request, 'Prodotto Aggiunto al carrello')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                ## altrimenti borse bracciali foulard
                else:
                    if CartItem.objects.filter(user_id = request.user.id).filter(composition_id=None).filter(product_id=post.product).filter(color_id=post.color):
                        ex_cart = CartItem.objects.filter(user_id = request.user.id).filter(composition_id=None).filter(color_id=post.color).get(product_id=post.product)
                        ex_cart.quantity += post.quantity
                        ex_cart.save()
                        messages.success(request, 'Prodotto già presente, abbiamo aggiornato la quantità')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
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
                #order = Order.objects.get(id=post.id)
                if cart.composition:
                    composition = Composition.objects.get(id=cart.composition_id)
                    check_magazzino(cart.quantity, cart.composition.quantity, composition)
                post_cart.save()

            cart_list.delete() #cancello carrello dopo ordine

            ### email
            ord_list = Order.objects.get(pk=post.id) 
            ordine = "ordine id: ordine effettuato da: " + request.user.username
            subject, from_email, to = ordine, request.user.email, 'info@bergeitalia.com'
            text_content = 'This is an important message.'
            html_content = render_to_string('order_email.html', {'post': ord_list})
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
                #return HttpResponseRedirect('/success/') # Redirect after POST
            #return redirect('/order', pk=post.pk)
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
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



# customer
def customer_page(request):
    order_list = Order.objects.filter(user_id=request.user.id).order_by('-id')
    fatt = Fatturazione.objects.filter(user_id=request.user.id).first
    ind = IndirizzoSpedizione.objects.filter(user_id=request.user.id).first
    context = {
                'order_list':order_list,
                'fatt':fatt,
                'ind':ind
                }
    return render_to_response('customer.html', context, context_instance=RequestContext(request))



def add_customer_fatturazione(request):
    if request.method == "POST":
            form = AddFormFatturazione(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.published_date = timezone.now()
                post.save()
                messages.success(request, 'Dati Fatturazione Inseriti')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                #return redirect('/', pk=post.pk)
            else:
                messages.error(request, 'Dati Fatturazione non inseriti')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Dati Fatturazione non inseriti')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def update_customer_fatturazione(request, pk=None):
    obj = get_object_or_404(Fatturazione, pk=pk)
    form = AddFormFatturazione(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
           form.save()
           messages.success(request, 'Dati Fatturazione Aggiornati')
           return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    messages.error(request, 'Dati Fatturazione non aggiornati')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def add_customer_indirizzo_spedizione(request):
    if request.method == "POST":
            form = AddFormIndirizzoSpredizione(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.published_date = timezone.now()
                post.save()
                messages.success(request, 'Dati Spedizione Inseriti')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                #return redirect('/', pk=post.pk)
            else:
                messages.error(request, 'Dati Spedizione non inseriti')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Dati Spedizione non inseriti')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def update_customer_indirizzo_spedizione(request, pk=None):
    obj = get_object_or_404(IndirizzoSpedizione, pk=pk)
    form = AddFormIndirizzoSpredizione(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
           form.save()
           messages.success(request, 'Dati Indirizzo Spedizione Aggiornati')
           return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    messages.error(request, 'Dati Indirizzo Spedizione non aggiornati')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



# search
def search(request):
    try:
        q = request.GET['q']
        product_list = Product.objects.filter(Q(name__icontains=q) | Q(code=q) | Q(descrizione__icontains=q) | Q(color__name__icontains=q) | Q(tags__name__in=q))
        return render_to_response('price_list.html', {'product_list':product_list, 'q':q}, context_instance=RequestContext(request))
    except KeyError:
        messages.error(request, 'Nessuna Corrispondenza Trovata')
        #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return render_to_response('price_list.html', context_instance=RequestContext(request))




#### CHARTS ###########
def charts(request):
    order_list =Order.objects.all()[:6]
    a = []
    b = []

    for order in order_list:
        a += [order.user.username]
        b += [order.tot_price]

    order_product = OrderItem.objects.values('product_id').annotate(total=Count('product_id')).order_by('-total')[:6]
    order_user = Order.objects.values('user').annotate(total=Count('user')).order_by('-user')[:6]

    context = {'order_list':order_list,
                'order_product':order_product,
                'order_user':order_user,
                'a':a,
                'b':b}
    return render_to_response('chart.html', context, context_instance=RequestContext(request))


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

            recipients = ['info@bergeitalia.com']
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


### setting language session
def language(request, language='it'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
